from fastapi import FastAPI


def make_app() -> FastAPI:
    app = FastAPI()

    return app


main = make_app()
