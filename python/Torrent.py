import libtorrent as lt
import time
import datetime

def download_torrent():
    ses = lt.session()
    ses.listen_on(6881, 6891)
    link ="magnet:?xt=urn:btih:CB02BB13F906536396C61A5042B68FC3011FE425&dn=Family.Guy.S17.Season.17.Complete.720p.WEBRip.x264-maximersk+%5Bmrsktv%5D&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451&tr=udp%3A%2F%2Ftracker.cyberia.is%3A6969%2Fannounce&tr=udp%3A%2F%2Fopen.demonii.si%3A1337%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.tiny-vps.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.iamhansen.xyz%3A2000%2Fannounce&tr=udp%3A%2F%2Fangietorrents.cc%2Fannounce&tr=udp%3A%2F%2F9.rarbg.me%3A2850%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=http%3A%2F%2Ftracker.openbittorrent.com%3A80%2Fannounce&tr=udp%3A%2F%2Fopentracker.i2p.rocks%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fcoppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.zer0day.to%3A1337%2Fannounce"
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
