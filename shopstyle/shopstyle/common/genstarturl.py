from shopstyle import spiderconf as Conf

def gen_urls(start_idx, totalnum):
    
    batch_size = 50
    start_urls = []
    i = start_idx
    while(i <= totalnum):
        start_urls.append(Conf.seed_url.format("dresses", 
                                        str(batch_size), 
                                        str(i), 
                                        "women"))
        i = i + batch_size
    return start_urls

