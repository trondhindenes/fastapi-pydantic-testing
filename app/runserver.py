from app.app_wrapper import app
import uvicorn


if __name__ == "__main__":
    uvicorn.run(
        app, host="0.0.0.0", port=9000, access_log=True,
    )
