from common.log import log, get_current_dir


log.info("hello")
log.warning("world")
log.error("hello world")
path = get_current_dir("report", "img", 'demo.png')
log.debug("hello world", path)
