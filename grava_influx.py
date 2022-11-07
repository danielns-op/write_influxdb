#!/usr/bin/python3
# -*- coding: utf-8 -*-
# - grava_influx.py ------------------------------------------------- #
# ------------------------------------------------------------------- #
# Author: Daniel Noronha da Silva C012743                             #
#  Email: danielns.py@gmail.com                                       #
# ------------------------------------------------------------------- #
# - Descrição ------------------------------------------------------- #
#   Script para gravação de dados no influxDB.                        #
# ------------------------------------------------------------------- #

# - Imports --------------------------------------------------------- #
from datetime import datetime
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
# ------------------------------------------------------------------- #

# - Classes --------------------------------------------------------- #
class GravaInfluxDB:
  def __init__(self, url, token, org, bucket, measurement):
    self.url = url
    self.token = token
    self.org = org
    self.bucket = bucket
    self.measurement = measurement

  def grava_influx(self, tag_dict, field_dict, time):
    client = InfluxDBClient(
      url=self.url,
      token=self.token,
      org=self.org)

    write_api = client.write_api(write_options=SYNCHRONOUS)
    write_api.write(self.bucket, self.org, {"measurement": self.measurement, "tags": tag_dict, "fields": field_dict, "time": time})
    client.close()


# ------------------------------------------------------------------- #
