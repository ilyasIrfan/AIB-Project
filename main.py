import fastapi
from fastapi.responses import FileResponse #aiofiles include

app = fastapi.FastAPI()

@app.get("/")
async def earthquake_cluster_analysis():
    return FileResponse("sumbawaEarthquake.png")