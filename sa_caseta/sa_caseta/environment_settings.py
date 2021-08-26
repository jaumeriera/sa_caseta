#!/usr/bin/env python
from decouple import config


class Settings:

    def __getattr__(self, attr):
        return config(attr)

    '''
            DATABASE settings
        '''

    @property
    def POSTGRES_USER(self):
        return config('POSTGRES_USER', default='udev')

    @property
    def POSTGRES_DB_NAME(self):
        return config('POSTGRES_DB_NAME', default='devdb')

    @property
    def POSTGRES_HOST(self):
        return config('POSTGRES_HOST', default='db')

    @property
    def POSTGRES_PORT(self):
        return config('POSTGRES_PORT', default='5432', cast=int)

    @property
    def POSTGRES_PASSWORD(self):
        return config('POSTGRES_PASSWORD', default='')

    '''
        DJANGO settings
    '''

    @property
    def DEBUG(self):
        return config('DEBUG', default=False, cast=bool)


settings = Settings()