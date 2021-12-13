import fastapi, json
from fastapi.responses import FileResponse #aiofiles include

app = fastapi.FastAPI()

with open("listOfRegion.json","r") as read_file:
	data = json.load(read_file)

@app.get("/region/")
async def most_frequent_earthquake_region_indonesia():
    return data

@app.get("/region/{region_id}/")
async def earthquake_cluster_analysis(region_id : int):
    if region_id == 1:
        return FileResponse("sumbawaEarthquake.png")
    elif region_id == 2:
        return FileResponse("MinahasaEarthQuake.png")
    elif region_id == 3:
        return FileResponse("JavaEarthQuake.png")
    else:
        raise fastapi.HTTPException(
			status_code = 404,
			detail = f'region not found. id range from 1 to 3'
		)