import pytest

from src.utils import StreamQueue, combine_sorted

from src.utils import AscendingEnforcedStreamQueue


@pytest.fixture
def first_list():
    return [
        "apple",
        "banana",
        "cabbage"
    ]


@pytest.fixture
def second_list():
    return [
        "aardvarks barking ceaselessly",
        "apt applicants angrily apply algorithms",
        "plutocrats pillaging peasants"
    ]


@pytest.fixture()
def third_list():
    return ["cabbage"]


@pytest.fixture
def improperly_sorted_list():
    return [
        "apt applicants angrily apply algorithms",
        "plutocrats pillaging peasants",
        "aardvarks barking ceaselessly",
    ]


@pytest.fixture()
def expected_result():
    return [
        "aardvarks barking ceaselessly",
        "apple",
        "apt applicants angrily apply algorithms",
        "banana",
        "cabbage",
        "plutocrats pillaging peasants"
    ]


def test_combine_sorted(first_list, second_list, expected_result):
    streams = [StreamQueue(first_list), StreamQueue(second_list)]

    assert list(combine_sorted(streams)) == expected_result


def test_dont_add_duplicates(first_list, second_list, third_list, expected_result):
    streams = [
        AscendingEnforcedStreamQueue(li) for li in [first_list, second_list, third_list]
        ]

    result = list(combine_sorted(streams))
    assert result == expected_result


def test_exception_with_improperly_sorted_input(first_list, improperly_sorted_list):
    streams = [AscendingEnforcedStreamQueue(first_list), AscendingEnforcedStreamQueue(improperly_sorted_list)]
    with pytest.raises(Exception):
        list(combine_sorted(streams))
