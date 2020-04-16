import argparse
import tracert as t


def main():
    parser = argparse.ArgumentParser("для каждого IP-адреса программа выводит результат трассировки "
                                     "и указывает номер автономной системы")
    parser.add_argument('-hostname', type=str, help='ip address')
    args = parser.parse_args()
    tracert = t.Tracert()
    tracert.get_path(args.hostname)


if __name__ == "__main__":
    main()
