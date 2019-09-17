"""Find window of time when most authors were active.

For example::

    >>> data = [
    ...    ('Alice', 1901, 1950),
    ...    ('Bob',   1920, 1960),
    ...    ('Carol', 1908, 1945),
    ...    ('Dave',  1951, 1960),
    ... ]

    >>> most_active(data)
    (1920, 1945)

(Alice, Bob, and Carol were all active then).

If there's more than one period, find the earliest::

    >>> data = [
    ...    ('Alice', 1901, 1950),
    ...    ('Bob',   1920, 1960),
    ...    ('Carol', 1908, 1945),
    ...    ('Dave',  1951, 1960),
    ...    ('Eve',   1955, 1985),
    ... ]

    >>> most_active(data)
    (1920, 1945)

(Alice, Bob, Carol were active 1920-1945. Bob, Dave, and Eve were active 1951-1960.
Since there's a tie, the first was returned)
"""


def most_active(bio_data):
    """Find window of time when most authors were active."""

    # if multiple, are they adjacent/do they overlap?
    # if yes, take full range. if no, take first range.

    date_set = set()
    for info in bio_data:
        date_set.update(info[1:])
    dates = sorted(list(date_set))

    active = {}
    for info in bio_data:
        for i in range(len(dates) - 1):
            span = (dates[i], dates[i + 1])
            # if span start and end between author start and end
            # author start <== span start; author end >= span end
            if info[1] <= span[0] and info[2] >= span[1]:
                active[span] = active.get(span, []) + [info[0]]

    max_len = 0
    max_spans = None
    for span, authors in active.items():
        if len(authors) > max_len:
            max_len = len(authors)
            max_spans = [span]
        elif len(authors) == max_len:
            max_spans += [span]

    if len(max_spans) > 1:
        start_date = max_spans[0][0]
        end_date = max_spans[0][1]
        for i in range(len(max_spans) - 1):
            if end_date >= max_spans[i + 1][0]:
                end_date = max_spans[i + 1][1]
    else:
        return max_spans[0]

    return (start_date, end_date)




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")