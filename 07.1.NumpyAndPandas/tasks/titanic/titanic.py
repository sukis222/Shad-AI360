import typing as tp

import pandas as pd

from pathlib import Path



def male_age(df: pd.DataFrame) -> float:
    """
    Return mean age of survived men, embarked in Southampton with fare > 30
    :param df: dataframe
    :return: mean age
    """

    return df[(df['Sex'] == 'male') & (df['Survived'] == 1) &
                                  (df['Fare'] > 30) & (df['Embarked'] == 'S') & (df['Age'].notna())]['Age'].mean()


def nan_columns(df: pd.DataFrame) -> tp.Iterable[str]:
    """
    Return list of columns containing nans
    :param df: dataframe
    :return: series of columns
    """
    ans = []
    for elem in df.keys():
        mask = df[elem].isna()
        if mask.sum() > 0:
            ans.append(elem)
    return df[ans]


def class_distribution(df: pd.DataFrame) -> pd.Series:
    """
    Return Pclass distrubution
    :param df: dataframe
    :return: series with ratios
    """

    gr1 = df[(df['Pclass'] == 1)]['Pclass'].size

    gr2 = df[(df['Pclass'] == 2)]['Pclass'].size

    gr3 = df[(df['Pclass'] == 3)]['Pclass'].size

    grs = gr1 + gr2 + gr3

    ans = pd.Series([gr1/grs, gr2/grs, gr3/grs], index=[1, 2, 3])

    return ans


def families_count(df: pd.DataFrame, k: int) -> int:
    """
    Compute number of families with more than k members
    :param df: dataframe,
    :param k: number of members,
    :return: number of families
    """
    happy_family = df['Name'].str.split(',')
    ans = happy_family.str[0].value_counts()
    return ans[ans > k].count()




def mean_price(df: pd.DataFrame, tickets: tp.Iterable[str]) -> float:
    """
    Return mean price for specific tickets list
    :param df: dataframe,
    :param tickets: list of tickets,
    :return: mean fare for this tickets
    """
    mean_fare = df[df['Ticket'].isin(tickets)]['Fare'].mean()
    return mean_fare


def max_size_group(df: pd.DataFrame, columns: list[str]) -> tp.Iterable[tp.Any]:
    """
    For given set of columns compute most common combination of values of these columns
    :param df: dataframe,
    :param columns: columns for grouping,
    :return: list of most common combination
    """
    max_size = df.groupby(columns).size().idxmax()
    return max_size

def is_luck(ticket: str) -> bool:
    """
    Determine if a ticket is lucky.
    :param ticket: ticket number
    :return: True if lucky, False otherwise
    """
    if not ticket.isdigit() or len(ticket) % 2 != 0:
        return False

    half_length = len(ticket) // 2
    left_side = sum([int(char) for char in ticket[:half_length]])
    right_side = sum([int(char) for char in ticket[half_length:]])

    return left_side == right_side

def dead_lucky(df: pd.DataFrame) -> float:
    """
    Compute dead ratio of passengers with lucky tickets.
    A ticket is considered lucky when it contains an even number of digits in it
    and the sum of the first half of digits equals the sum of the second part of digits
    ex:
    lucky: 123222, 2671, 935755
    not lucky: 123456, 62869, 568290
    :param df: dataframe,
    :return: ratio of dead lucky passengers
    """
    luck = df[df['Ticket'].apply(is_luck)]
    result = luck['Survived'].value_counts(normalize=True).get(0, 0)
    return result


