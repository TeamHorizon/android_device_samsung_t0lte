# Copyright (C) 2012 The Android Open Source Project
# Copyright (C) 2013 The CyanogenMod Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

""" Custom OTA commands for t0lte """

def FullOTA_InstallEnd(info):
  info.script.AppendExtra('ifelse(is_mounted("/data"), unmount("/data"));')
  info.script.AppendExtra('mount("ext4", "EMMC", "/dev/block/platform/dw_mmc/by-name/USERDATA", "/data", "");')
  info.script.AppendExtra('run_program("/sbin/sh", "-c", "busybox mkdir -p /data/cfw");')
  info.script.AppendExtra('run_program("/sbin/sh", "-c", "busybox cp /system/vendor/firmware/SlimISP_*.bin /data/cfw/");')
  info.script.AppendExtra('run_program("/sbin/sh", "-c", "busybox chown 1000 /data/cfw");')
  info.script.AppendExtra('run_program("/sbin/sh", "-c", "busybox chgrp 1013 /data/cfw");')
  info.script.AppendExtra('run_program("/sbin/sh", "-c", "busybox chmod 0775 /data/cfw");')
  info.script.AppendExtra('unmount("/data");')
