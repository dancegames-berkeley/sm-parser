source .env
python3 -m venv .venv
source .venv/bin/activate
python3 ./sm_parser.py
if $LOCAL; then
    cp songs.json /home/remy/Desktop/proj/test/songs.json
    echo "Songs transferred to local directory"
else
    scp songs.json dgab@apphost.ocf.berkeley.edu:/home/d/dg/dgab/songs.json
    echo "Songs transferred to OCF server"
fi
python3 ./image_parser.py
if $LOCAL; then
    cp -rt banner /home/remy/Desktop/proj/test/banner
    echo "Banner images transferred to local directory"
else
    scp -r banner dgab@apphost.ocf.berkeley.edu:/home/d/dg/dgab/banner
    echo "Banner images transferred to OCF server"
fi