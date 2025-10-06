set -ex 
git checkout tags/2.0.0 ./demos/as_builts/building_0001/space_123/latest.zip 
python distech/scripts/purge_backups.py
python distech/scripts/upload_latest.py
python distech/scripts/restore_latest.py
printf "Restored latest backup, controller will now reboot...\n"
sleep 5
until curl --output /dev/null --silent --head --fail "http://$DISTECH_DEVICE.local:443"; do
    printf 'Waiting for webserver...\n'
    sleep 5
done
printf "Controller is back online\n"
