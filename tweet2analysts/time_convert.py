def leapYear(y):
    if y % 400 == 0:
        return 1
    elif y % 4 == 0 and y % 100 != 0:
        return 1
    else:
        return 0


def month_add(timeOrigin):
    year = timeOrigin[0]
    leap = leapYear(year)
    if leap == 1:
        m_d = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        m_d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if timeOrigin[2] > m_d[(timeOrigin[1] - 1)]:
        if timeOrigin[1] == 12:
            timeOrigin[1] = 1
            timeOrigin[1] = 1
            timeOrigin[0] += 1
        else:
            timeOrigin[2] = 1
            timeOrigin[1] += 1
    return timeOrigin


if __name__ == '__main__':
    print("Hello, World!")
