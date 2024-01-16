from fastapi import FastAPI


class Singleton:
    _instance = None

    @classmethod
    def create_instance(cls, instance):
        cls._instance = instance

    def __new__(cls):
        if not cls._instance:
            raise Exception(f"{cls.__name__} class is not initialized")
        return cls._instance


class App(Singleton, FastAPI):
    pass
