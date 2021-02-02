from services.process_rise_drops import RiseDropProcessor


def main():
    a = RiseDropProcessor([(1, 5, 10), (4, 6, 8), (10, 15, 10), (11, 12, 8)])
    a.process_rise_and_drops()
    print(a.result_set)

    a = RiseDropProcessor([(1, 10, 4), (1, 8, 6), (1, 6, 8)])
    a.process_rise_and_drops()
    print(a.result_set)

    a = RiseDropProcessor([(0, 6, 2), (5, 10, 8), (7, 8, 12)])
    a.process_rise_and_drops()
    print(a.result_set)


if __name__ == "__main__":
    main()
