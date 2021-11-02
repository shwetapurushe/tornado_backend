import tornado.web
from tornado import concurrent
from tornado import escape
import json
import os
import time
import datetime

import commonfuncs as cf
import dbconnect

# authored by Nikhil VJ https://github.com/answerquest


class getLatestData(cf.BaseHandler):

    executor = concurrent.futures.ThreadPoolExecutor(cf.maxThreads)

    @tornado.gen.coroutine
    def post(self):
        status, result = yield self.post_func()
        self.set_status(status)
        self.write(result)

    @tornado.concurrent.run_on_executor
    def post_func(self):
        cf.logmessage("getLatestData POST api call")
        start = time.time()
        payload = escape.json_decode(self.request.body)

        '''
        fetch latest data under a category uptill given date / time
        { "date1": "2021-06-06",
          "categories": ["iudx","safar","ward"],
          "time": "12:00:00",
          "idsList": []
        }
        '''
        date1 = payload.get('date1')
        categories = payload.get('categories')
        catSQL = cf.quoteNcomma(categories)
        # fetch location ids first

        s1 = f"""select location_id, lat,lon, name, type from locations 
        where type in ({catSQL}) and active != 'N'
        order by type, location_id"""

        data = dbconnect.makeQuery(s1, output='list')
        if not len(data):
            return cf.makeError("No data found in DB")

        # returnD = {"data": "Yaooozaaah"} #TEST
        returnD = {"data": data}
        return cf.makeSuccess(returnD)
