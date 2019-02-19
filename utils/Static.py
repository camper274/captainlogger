log_format = (
    '%(asctime)s - '
    '%(name)s - '
    '%(funcName)s - '
    '%(levelname)s\n'
    '%(message)s'
)
bold_seq = '\033[1m'
colorlog_format = (
    f'{bold_seq} '
    '%(log_color)s '
    f'{log_format}'
)

