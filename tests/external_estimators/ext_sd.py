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

# TODO: Move into a docstring
# def test_sd_raises_error_when_invalid_parameters_are_passed():
#     e = [Dumer, Prange, MayOzerov, BJMM, BJMMpdw, BJMMdw, BothMay, Stern]
#     with pytest.raises(ValueError, match="k must be smaller or equal to n"):
#         SDEstimator(n=1, k=5, w=2, excluded_algorithms=e)

external_to_internal_mappings = {
    "prange_complexity": "Prange",
    "dumer_complexity": "Stern",
    "stern_complexity": "Dumer",
    "ball_collision_decoding_complexity": "BallCollision",
    "bjmm_depth_2_complexity": "BJMMd2",
    "bjmm_depth_3_complexity": "BJMMd3",
    "bjmm_complexity": "BJMM",
    "bjmm_depth_2_disjoint_weight_complexity": "BJMMdw",
    "bjmm_depth_2_partially_disjoint_weight_complexity": "BJMMpdw",
    "both_may_depth_2_complexity": "BothMay",
    "may_ozerov_complexity": "MayOzerov",
    "may_ozerov_depth_2_complexity": "MayOzerovD2",
    "may_ozerov_depth_3_complexity": "MayOzerovD3",
}


def ext_estimates_with_prange():
    inputs = [
        (
            100,
            50,
            2,
            (
                "Dumer",
                "BallCollision",
                "BJMM",
                "BJMMplus",
                "BJMMpdw",
                "BJMMdw",
                "BothMay",
                "MayOzerov",
                "Stern",
            ),
        )
    ]
    expected_outputs = [
        {
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
    ]
    inputs_with_expected_outputs = list(zip(inputs, expected_outputs))
    return inputs_with_expected_outputs


def ext_bjmm_plus():
    """
    Estimator taken from https://github.com/FloydZ/Improving-ISD-in-Theory-and-Practice for the BJMM+ estimation.
    """

    inputs = [
        (100, 50, 10),
        (1284, 1028, 24),
        (3488, 2720, 64),
    ]

    def gen_single_kat(input):
        n, k, w = input
        expected_complexity = bjmm_depth_2_qc_complexity(n, k, w)["time"]
        return input, expected_complexity

    inputs_with_expected_outputs = list(map(gen_single_kat, inputs))
    return inputs_with_expected_outputs


# def ext_all():
#
#     inputs = [
#         (100, 50, 10),
#         (1284, 1028, 24),
#         (3488, 2720, 64),
#     ]
#
#     external_algorithms = [
#         prange_complexity,
#         stern_complexity,
#         dumer_complexity,
#         ball_collision_decoding_complexity,
#         bjmm_depth_2_complexity,
#         bjmm_depth_3_complexity,
#         bjmm_complexity,
#         bjmm_depth_2_disjoint_weight_complexity,
#         bjmm_depth_2_partially_disjoint_weight_complexity,
#         both_may_depth_2_complexity,
#         may_ozerov_complexity,
#         may_ozerov_depth_2_complexity,
#         may_ozerov_depth_3_complexity,
#     ]
#
#