import libtorrent as lt
import time
import datetime

def download_torrent():
    ses = lt.session()
    ses.listen_on(6881, 6891)
    link ="magnet:?xt=urn:btih:CB02BB13F906536396C61A5042B68FC3011FE425"
    print(link)

    handle = lt.add_magnet_uri(ses, link, params)
    # change the 0 to a 1 to download sequential - this sequential option is only if you selected zip. If not,
    # scroll farther down.
    handle.set_sequential_download(0)

    ses.start_dht()
    begin = time.time()
    print(datetime.datetime.now())

    print('Downloading Metadata...')
    while not handle.has_metadata():
        time.sleep(1)
    print('Got Metadata, Starting Torrent Download...')

    print("Starting", handle.name())

    while handle.status().state != lt.torrent_status.seeding:
        s = handle.status()
        state_str = ['queued', 'checking', 'downloading metadata',
                     'downloading', 'finished', 'seeding', 'allocating']
        print('%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s ' % \
              (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, \
               s.num_peers, state_str[s.state]))
        time.sleep(10)

    end = time.time()
    print(handle.name(), "COMPLETE")

    print("Elapsed Time: ", int((end - begin) // 60), "min :", int((end - begin) % 60), "sec")

    print(datetime.datetime.now())


params = {
    'save_path': '.',
    'storage_mode': lt.storage_mode_t(2),
}
download_torrent()

print('\nALL DONE!')
