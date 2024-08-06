from storages.backends.s3 import S3Storage


class MediaS3Storage(S3Storage):
    location = "media"
    file_overwrite = False
