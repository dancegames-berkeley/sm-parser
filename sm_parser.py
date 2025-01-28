import simfile.dir
from simfile.base import BaseChart
from simfile.ssc import SSCChart
import os
import orjson
from dataclasses import dataclass


songs_path = '/home/dance/Desktop/Songs'

@dataclass
class ChartDetails:
    meter: str
    difficulty: str
    credit: str
    steps_type: str

@dataclass
class SongDetails:
    title: str
    artist: str
    credit: str
    banner: str
    charts: list[ChartDetails]

@dataclass
class PackDetails:
    title: str
    banner: str
    songs: list[SongDetails]

def parser():
    data: list[PackDetails] = []
    packs = os.listdir(songs_path)
    for pack in packs:
        try:
            pack = simfile.dir.SimfilePack(os.path.join(songs_path, pack))
        except:
            continue
        songs = []
        try:
            for song in pack.simfiles():
                song_data = SongDetails
                charts_list = []
                for chart in song.charts:
                    chart: BaseChart = chart
                    chart_data = ChartDetails(
                        meter = chart.meter,
                        difficulty = chart.difficulty,
                        credit = chart.credit if isinstance(chart, SSCChart) else None,
                        steps_type = chart.stepstype
                    )
                    charts_list.append(chart_data)

                song_data = SongDetails(
                    title = song.title,
                    artist = song.artist,
                    credit = song.credit,
                    banner = song.banner,
                    charts = charts_list
                )
                songs.append(song_data)
        except Exception as e:
            print(f'Error processing song: {e}')
            continue
        
        pack_data = PackDetails(
            title = pack.name,
            banner = pack.banner(),
            songs = songs
        )
        data.append(pack_data)

    with open('songs.json', 'wb') as file:
        file.write(orjson.dumps(data, option=orjson.OPT_INDENT_2))

parser()