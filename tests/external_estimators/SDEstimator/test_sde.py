import pytest
from cryptographic_estimators.SDEstimator import (
    SDProblem,
    SDEstimator,
    Prange,
    Dumer,
    BallCollision,
    BJMM,
    BJMMdw,
    BJMMpdw,
    BothMay,
    MayOzerov,
    Stern,
    BJMMplus,
)
from cryptographic_estimators.SDEstimator.SDAlgorithms import (
    Prange,
    Dumer,
    BallCollision,
    BJMMd2,
    BJMMd3,
    BJMM,
    BJMMdw,
    BJMMpdw,
    BothMay,
    MayOzerov,
    MayOzerovD2,
    MayOzerovD3,
    Stern,
    BJMMplus,
)
from tests.external_estimators.helpers.optimize import bjmm_depth_2_qc_complexity
from tests.external_estimators.helpers.estimator import (
    prange_complexity,
    dumer_complexity,
    stern_complexity,
    ball_collision_decoding_complexity,
    bjmm_depth_2_complexity,
    bjmm_depth_3_complexity,
    bjmm_complexity,
    bjmm_depth_2_disjoint_weight_complexity,
    bjmm_depth_2_partially_disjoint_weight_complexity,
    both_may_depth_2_complexity,
    may_ozerov_complexity,
    may_ozerov_depth_2_complexity,
    may_ozerov_depth_3_complexity,
)


def test_sd_raises_error_when_invalid_parameters_are_passed():
    e = [Dumer, Prange, MayOzerov, BJMM, BJMMpdw, BJMMdw, BothMay, Stern]
    with pytest.raises(ValueError, match="k must be smaller or equal to n"):
        SDEstimator(n=1, k=5, w=2, excluded_algorithms=e)


def test_estimates_with_prange():
    excluded_algorithms = [
        Dumer,
        BallCollision,
        BJMM,
        BJMMplus,
        BJMMpdw,
        BJMMdw,
        BothMay,
        MayOzerov,
        Stern,
    ]
    sd_estimator = SDEstimator(100, 50, 2, excluded_algorithms=excluded_algorithms)
    result = sd_estimator.estimate()
    expected_result = {
        "Prange": {
            "additional_information": {
                "gauss": 10.929258408636972,
                "permutations": 2.014646775964401,
            },
            "estimate": {
                "memory": 12.688250309133178,
                "parameters": {"r": 4},
                "time": 19.587761374376097,
            },
        }
    }
    assert result == expected_result


ranges = 0.01

test_sets = [
    [100, 50, 10],
    [1284, 1028, 24],
    [3488, 2720, 64],
]

algos = [
    Prange,
    Stern,
    Dumer,
    BallCollision,
    BJMMd2,
    BJMMd3,
    BJMM,
    BJMMdw,
    BJMMpdw,
    BothMay,
    MayOzerov,
    MayOzerovD2,
    MayOzerovD3,
]

test_algos = [
    prange_complexity,
    stern_complexity,
    dumer_complexity,
    ball_collision_decoding_complexity,
    bjmm_depth_2_complexity,
    bjmm_depth_3_complexity,
    bjmm_complexity,
    bjmm_depth_2_disjoint_weight_complexity,
    bjmm_depth_2_partially_disjoint_weight_complexity,
    both_may_depth_2_complexity,
    may_ozerov_complexity,
    may_ozerov_depth_2_complexity,
    may_ozerov_depth_3_complexity,
]


def test_all():
    """
    tests that all estimations match those from https://github.com/Crypto-TII/syndrome_decoding_estimator up to
    a tolerance of 0.01 bit
    """
    assert len(algos) == len(test_algos)
    for i, _ in enumerate(test_algos):
        internal_algorithm = algos[i]
        external_algorithm = test_algos[i]
        for set in test_sets:
            n, k, w = set[0], set[1], set[2]
            internal_estimator = internal_algorithm(
                SDProblem(n=n, k=k, w=w), bit_complexities=0
            )
            external_estimator = external_algorithm(n=n, k=k, w=w)

            # Slight correction of parameter ranges leads to (slightly) better parameters in case of the
            # CryptographicEstimators for Both-May and May-Ozerov. For test we fix parameters to the once from the
            # online code.
            if (
                internal_estimator._name == "Both-May"
                or internal_estimator._name == "May-OzerovD2"
                or internal_estimator._name == "May-OzerovD3"
            ):
                too_much = [
                    i
                    for i in external_estimator["parameters"]
                    if i not in internal_estimator.parameter_names()
                ]
                for i in too_much:
                    external_estimator["parameters"].pop(i)
                internal_estimator.set_parameters(external_estimator["parameters"])

            actual_complexity = internal_estimator.time_complexity()
            expected_complexity = external_estimator["time"]
            assert (
                expected_complexity - ranges
                <= actual_complexity
                <= expected_complexity + ranges
            )


def test_bjmm_plus():
    """
    tests that BJMM+ estimation matches the one from https://github.com/FloydZ/Improving-ISD-in-Theory-and-Practice
     up to a tolerance of 0.01 bit
    """
    for set in test_sets:
        n, k, w = set[0], set[1], set[2]
        t = bjmm_depth_2_qc_complexity(n, k, w)
        t1 = t["time"]
        t2 = BJMMplus(SDProblem(n, k, w), bit_complexities=0).time_complexity()
        assert t1 - ranges <= t2 <= t1 + ranges


if __name__ == "__main__":
    test_all()
    test_bjmm_plus()
