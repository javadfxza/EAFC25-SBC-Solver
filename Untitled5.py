{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Iou5FPOoH_rj",
        "outputId": "01640f4e-bd96-4a00-bdca-cecb81a42cce"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting selenium\n",
            "  Downloading selenium-4.29.0-py3-none-any.whl.metadata (7.1 kB)\n",
            "Requirement already satisfied: urllib3<3,>=1.26 in /usr/local/lib/python3.11/dist-packages (from urllib3[socks]<3,>=1.26->selenium) (2.3.0)\n",
            "Collecting trio~=0.17 (from selenium)\n",
            "  Downloading trio-0.29.0-py3-none-any.whl.metadata (8.5 kB)\n",
            "Collecting trio-websocket~=0.9 (from selenium)\n",
            "  Downloading trio_websocket-0.12.2-py3-none-any.whl.metadata (5.1 kB)\n",
            "Requirement already satisfied: certifi>=2021.10.8 in /usr/local/lib/python3.11/dist-packages (from selenium) (2025.1.31)\n",
            "Requirement already satisfied: typing_extensions~=4.9 in /usr/local/lib/python3.11/dist-packages (from selenium) (4.12.2)\n",
            "Requirement already satisfied: websocket-client~=1.8 in /usr/local/lib/python3.11/dist-packages (from selenium) (1.8.0)\n",
            "Requirement already satisfied: attrs>=23.2.0 in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (25.1.0)\n",
            "Requirement already satisfied: sortedcontainers in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (2.4.0)\n",
            "Requirement already satisfied: idna in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (3.10)\n",
            "Collecting outcome (from trio~=0.17->selenium)\n",
            "  Downloading outcome-1.3.0.post0-py2.py3-none-any.whl.metadata (2.6 kB)\n",
            "Requirement already satisfied: sniffio>=1.3.0 in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (1.3.1)\n",
            "Collecting wsproto>=0.14 (from trio-websocket~=0.9->selenium)\n",
            "  Downloading wsproto-1.2.0-py3-none-any.whl.metadata (5.6 kB)\n",
            "Requirement already satisfied: pysocks!=1.5.7,<2.0,>=1.5.6 in /usr/local/lib/python3.11/dist-packages (from urllib3[socks]<3,>=1.26->selenium) (1.7.1)\n",
            "Requirement already satisfied: h11<1,>=0.9.0 in /usr/local/lib/python3.11/dist-packages (from wsproto>=0.14->trio-websocket~=0.9->selenium) (0.14.0)\n",
            "Downloading selenium-4.29.0-py3-none-any.whl (9.5 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m9.5/9.5 MB\u001b[0m \u001b[31m53.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading trio-0.29.0-py3-none-any.whl (492 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m492.9/492.9 kB\u001b[0m \u001b[31m20.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading trio_websocket-0.12.2-py3-none-any.whl (21 kB)\n",
            "Downloading outcome-1.3.0.post0-py2.py3-none-any.whl (10 kB)\n",
            "Downloading wsproto-1.2.0-py3-none-any.whl (24 kB)\n",
            "Installing collected packages: wsproto, outcome, trio, trio-websocket, selenium\n",
            "Successfully installed outcome-1.3.0.post0 selenium-4.29.0 trio-0.29.0 trio-websocket-0.12.2 wsproto-1.2.0\n",
            "Hit:1 http://archive.ubuntu.com/ubuntu jammy InRelease\n",
            "Get:2 http://archive.ubuntu.com/ubuntu jammy-updates InRelease [128 kB]\n",
            "Get:3 http://security.ubuntu.com/ubuntu jammy-security InRelease [129 kB]\n",
            "Get:4 https://cloud.r-project.org/bin/linux/ubuntu jammy-cran40/ InRelease [3,632 B]\n",
            "Get:5 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64  InRelease [1,581 B]\n",
            "Get:6 https://r2u.stat.illinois.edu/ubuntu jammy InRelease [6,555 B]\n",
            "Get:7 http://archive.ubuntu.com/ubuntu jammy-backports InRelease [127 kB]\n",
            "Hit:8 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy InRelease\n",
            "Hit:9 https://ppa.launchpadcontent.net/graphics-drivers/ppa/ubuntu jammy InRelease\n",
            "Hit:10 https://ppa.launchpadcontent.net/ubuntugis/ppa/ubuntu jammy InRelease\n",
            "Get:11 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64  Packages [1,370 kB]\n",
            "Get:12 https://r2u.stat.illinois.edu/ubuntu jammy/main amd64 Packages [2,668 kB]\n",
            "Get:13 http://archive.ubuntu.com/ubuntu jammy-updates/universe amd64 Packages [1,533 kB]\n",
            "Get:14 https://r2u.stat.illinois.edu/ubuntu jammy/main all Packages [8,731 kB]\n",
            "Get:15 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 Packages [2,988 kB]\n",
            "Get:16 http://archive.ubuntu.com/ubuntu jammy-updates/restricted amd64 Packages [3,934 kB]\n",
            "Get:17 http://security.ubuntu.com/ubuntu jammy-security/main amd64 Packages [2,682 kB]\n",
            "Get:18 http://security.ubuntu.com/ubuntu jammy-security/universe amd64 Packages [1,235 kB]\n",
            "Fetched 25.5 MB in 4s (5,908 kB/s)\n",
            "Reading package lists... Done\n",
            "W: Skipping acquire of configured file 'main/source/Sources' as repository 'https://r2u.stat.illinois.edu/ubuntu jammy InRelease' does not seem to provide it (sources.list entry misspelt?)\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "The following additional packages will be installed:\n",
            "  apparmor chromium-browser libfuse3-3 liblzo2-2 snapd squashfs-tools systemd-hwe-hwdb udev\n",
            "Suggested packages:\n",
            "  apparmor-profiles-extra apparmor-utils fuse3 zenity | kdialog\n",
            "The following NEW packages will be installed:\n",
            "  apparmor chromium-browser chromium-chromedriver libfuse3-3 liblzo2-2 snapd squashfs-tools\n",
            "  systemd-hwe-hwdb udev\n",
            "0 upgraded, 9 newly installed, 0 to remove and 31 not upgraded.\n",
            "Need to get 30.3 MB of archives.\n",
            "After this operation, 123 MB of additional disk space will be used.\n",
            "Get:1 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 apparmor amd64 3.0.4-2ubuntu2.4 [598 kB]\n",
            "Get:2 http://archive.ubuntu.com/ubuntu jammy/main amd64 liblzo2-2 amd64 2.10-2build3 [53.7 kB]\n",
            "Get:3 http://archive.ubuntu.com/ubuntu jammy/main amd64 squashfs-tools amd64 1:4.5-3build1 [159 kB]\n",
            "Get:4 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 udev amd64 249.11-0ubuntu3.12 [1,557 kB]\n",
            "Get:5 http://archive.ubuntu.com/ubuntu jammy/main amd64 libfuse3-3 amd64 3.10.5-1build1 [81.2 kB]\n",
            "Get:6 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 snapd amd64 2.67.1+22.04 [27.8 MB]\n",
            "Get:7 http://archive.ubuntu.com/ubuntu jammy-updates/universe amd64 chromium-browser amd64 1:85.0.4183.83-0ubuntu2.22.04.1 [49.2 kB]\n",
            "Get:8 http://archive.ubuntu.com/ubuntu jammy-updates/universe amd64 chromium-chromedriver amd64 1:85.0.4183.83-0ubuntu2.22.04.1 [2,308 B]\n",
            "Get:9 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 systemd-hwe-hwdb all 249.11.5 [3,228 B]\n",
            "Fetched 30.3 MB in 1s (40.3 MB/s)\n",
            "Preconfiguring packages ...\n",
            "Selecting previously unselected package apparmor.\n",
            "(Reading database ... 124947 files and directories currently installed.)\n",
            "Preparing to unpack .../0-apparmor_3.0.4-2ubuntu2.4_amd64.deb ...\n",
            "Unpacking apparmor (3.0.4-2ubuntu2.4) ...\n",
            "Selecting previously unselected package liblzo2-2:amd64.\n",
            "Preparing to unpack .../1-liblzo2-2_2.10-2build3_amd64.deb ...\n",
            "Unpacking liblzo2-2:amd64 (2.10-2build3) ...\n",
            "Selecting previously unselected package squashfs-tools.\n",
            "Preparing to unpack .../2-squashfs-tools_1%3a4.5-3build1_amd64.deb ...\n",
            "Unpacking squashfs-tools (1:4.5-3build1) ...\n",
            "Selecting previously unselected package udev.\n",
            "Preparing to unpack .../3-udev_249.11-0ubuntu3.12_amd64.deb ...\n",
            "Unpacking udev (249.11-0ubuntu3.12) ...\n",
            "Selecting previously unselected package libfuse3-3:amd64.\n",
            "Preparing to unpack .../4-libfuse3-3_3.10.5-1build1_amd64.deb ...\n",
            "Unpacking libfuse3-3:amd64 (3.10.5-1build1) ...\n",
            "Selecting previously unselected package snapd.\n",
            "Preparing to unpack .../5-snapd_2.67.1+22.04_amd64.deb ...\n",
            "Unpacking snapd (2.67.1+22.04) ...\n",
            "Setting up apparmor (3.0.4-2ubuntu2.4) ...\n",
            "Created symlink /etc/systemd/system/sysinit.target.wants/apparmor.service → /lib/systemd/system/apparmor.service.\n",
            "Setting up liblzo2-2:amd64 (2.10-2build3) ...\n",
            "Setting up squashfs-tools (1:4.5-3build1) ...\n",
            "Setting up udev (249.11-0ubuntu3.12) ...\n",
            "invoke-rc.d: could not determine current runlevel\n",
            "invoke-rc.d: policy-rc.d denied execution of start.\n",
            "Setting up libfuse3-3:amd64 (3.10.5-1build1) ...\n",
            "Setting up snapd (2.67.1+22.04) ...\n",
            "Created symlink /etc/systemd/system/multi-user.target.wants/snapd.apparmor.service → /lib/systemd/system/snapd.apparmor.service.\n",
            "Created symlink /etc/systemd/system/multi-user.target.wants/snapd.autoimport.service → /lib/systemd/system/snapd.autoimport.service.\n",
            "Created symlink /etc/systemd/system/multi-user.target.wants/snapd.core-fixup.service → /lib/systemd/system/snapd.core-fixup.service.\n",
            "Created symlink /etc/systemd/system/multi-user.target.wants/snapd.recovery-chooser-trigger.service → /lib/systemd/system/snapd.recovery-chooser-trigger.service.\n",
            "Created symlink /etc/systemd/system/multi-user.target.wants/snapd.seeded.service → /lib/systemd/system/snapd.seeded.service.\n",
            "Created symlink /etc/systemd/system/cloud-final.service.wants/snapd.seeded.service → /lib/systemd/system/snapd.seeded.service.\n",
            "Unit /lib/systemd/system/snapd.seeded.service is added as a dependency to a non-existent unit cloud-final.service.\n",
            "Created symlink /etc/systemd/system/multi-user.target.wants/snapd.service → /lib/systemd/system/snapd.service.\n",
            "Created symlink /etc/systemd/system/timers.target.wants/snapd.snap-repair.timer → /lib/systemd/system/snapd.snap-repair.timer.\n",
            "Created symlink /etc/systemd/system/sockets.target.wants/snapd.socket → /lib/systemd/system/snapd.socket.\n",
            "Created symlink /etc/systemd/system/final.target.wants/snapd.system-shutdown.service → /lib/systemd/system/snapd.system-shutdown.service.\n",
            "Selecting previously unselected package chromium-browser.\n",
            "(Reading database ... 125384 files and directories currently installed.)\n",
            "Preparing to unpack .../chromium-browser_1%3a85.0.4183.83-0ubuntu2.22.04.1_amd64.deb ...\n",
            "=> Installing the chromium snap\n",
            "==> Checking connectivity with the snap store\n",
            "===> System doesn't have a working snapd, skipping\n",
            "Unpacking chromium-browser (1:85.0.4183.83-0ubuntu2.22.04.1) ...\n",
            "Selecting previously unselected package chromium-chromedriver.\n",
            "Preparing to unpack .../chromium-chromedriver_1%3a85.0.4183.83-0ubuntu2.22.04.1_amd64.deb ...\n",
            "Unpacking chromium-chromedriver (1:85.0.4183.83-0ubuntu2.22.04.1) ...\n",
            "Selecting previously unselected package systemd-hwe-hwdb.\n",
            "Preparing to unpack .../systemd-hwe-hwdb_249.11.5_all.deb ...\n",
            "Unpacking systemd-hwe-hwdb (249.11.5) ...\n",
            "Setting up systemd-hwe-hwdb (249.11.5) ...\n",
            "Setting up chromium-browser (1:85.0.4183.83-0ubuntu2.22.04.1) ...\n",
            "update-alternatives: using /usr/bin/chromium-browser to provide /usr/bin/x-www-browser (x-www-browser) in auto mode\n",
            "update-alternatives: using /usr/bin/chromium-browser to provide /usr/bin/gnome-www-browser (gnome-www-browser) in auto mode\n",
            "Setting up chromium-chromedriver (1:85.0.4183.83-0ubuntu2.22.04.1) ...\n",
            "Processing triggers for udev (249.11-0ubuntu3.12) ...\n",
            "Processing triggers for mailcap (3.70+nmu1ubuntu1) ...\n",
            "Processing triggers for hicolor-icon-theme (0.17-2) ...\n",
            "Processing triggers for libc-bin (2.35-0ubuntu3.8) ...\n",
            "/sbin/ldconfig.real: /usr/local/lib/libur_adapter_level_zero.so.0 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtbbmalloc.so.2 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libhwloc.so.15 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtcm.so.1 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtbb.so.12 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtbbbind_2_5.so.3 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libur_adapter_opencl.so.0 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtbbmalloc_proxy.so.2 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libur_loader.so.0 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libumf.so.0 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtbbbind_2_0.so.3 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtbbbind.so.3 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtcm_debug.so.1 is not a symbolic link\n",
            "\n",
            "Processing triggers for man-db (2.10.2-1) ...\n",
            "Processing triggers for dbus (1.12.20-2ubuntu4.1) ...\n",
            "cp: '/usr/lib/chromium-browser/chromedriver' and '/usr/bin/chromedriver' are the same file\n",
            "Collecting webdriver_manager\n",
            "  Downloading webdriver_manager-4.0.2-py2.py3-none-any.whl.metadata (12 kB)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.11/dist-packages (from webdriver_manager) (2.32.3)\n",
            "Collecting python-dotenv (from webdriver_manager)\n",
            "  Downloading python_dotenv-1.0.1-py3-none-any.whl.metadata (23 kB)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.11/dist-packages (from webdriver_manager) (24.2)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests->webdriver_manager) (3.4.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests->webdriver_manager) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests->webdriver_manager) (2.3.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests->webdriver_manager) (2025.1.31)\n",
            "Downloading webdriver_manager-4.0.2-py2.py3-none-any.whl (27 kB)\n",
            "Downloading python_dotenv-1.0.1-py3-none-any.whl (19 kB)\n",
            "Installing collected packages: python-dotenv, webdriver_manager\n",
            "Successfully installed python-dotenv-1.0.1 webdriver_manager-4.0.2\n"
          ]
        }
      ],
      "source": [
        "!pip install selenium\n",
        "!apt-get update # برای نصب وابستگی‌های Chrome\n",
        "!apt install -y chromium-chromedriver\n",
        "!cp /usr/lib/chromium-browser/chromedriver /usr/bin\n",
        "!pip install webdriver_manager\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "from selenium.webdriver.common.by import By\n"
      ],
      "metadata": {
        "id": "QUnEI96pIRRM"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "options = Options()\n",
        "options.headless = True\n",
        "options.add_argument('--no-sandbox')\n",
        "options.add_argument('--disable-dev-shm-usage')\n"
      ],
      "metadata": {
        "id": "RayS_ssvIVKO"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "driver = webdriver.Chrome('chromedriver', options=options)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 141
        },
        "id": "Zj-i56eWIYgZ",
        "outputId": "8403766e-0723-47a3-fadd-514e999e1b08"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "error",
          "ename": "TypeError",
          "evalue": "WebDriver.__init__() got multiple values for argument 'options'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-4-8c7163c36cc6>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mdriver\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'chromedriver'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m: WebDriver.__init__() got multiple values for argument 'options'"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=options)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 141
        },
        "id": "5v7xIwurIoP3",
        "outputId": "547eaa2f-ad18-452b-946b-3d0f42491fe5"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "error",
          "ename": "TypeError",
          "evalue": "WebDriver.__init__() got an unexpected keyword argument 'executable_path'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-5-0661388233ab>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mdriver\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mexecutable_path\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m'/usr/bin/chromedriver'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m: WebDriver.__init__() got an unexpected keyword argument 'executable_path'"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# نصب پکیج‌ها\n",
        "!pip install selenium\n",
        "!apt-get update # برای نصب وابستگی‌های Chrome\n",
        "!apt install -y chromium-chromedriver\n",
        "!cp /usr/lib/chromium-browser/chromedriver /usr/bin\n",
        "!pip install webdriver_manager\n",
        "\n",
        "# وارد کردن کتابخانه‌ها\n",
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "from selenium.webdriver.common.by import By\n",
        "\n",
        "# تنظیمات Chrome برای Colab\n",
        "options = Options()\n",
        "options.headless = True\n",
        "options.add_argument('--no-sandbox')\n",
        "options.add_argument('--disable-dev-shm-usage')\n",
        "\n",
        "# راه‌اندازی WebDriver\n",
        "driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=options)\n",
        "\n",
        "# استخراج داده‌ها از سایت\n",
        "driver.get('https://www.futbin.com/squad-building-challenges')\n",
        "sbc_items = driver.find_elements(By.CLASS_NAME, 'sbc-item')\n",
        "sbc_list = []\n",
        "\n",
        "for sbc in sbc_items:\n",
        "    sbc_name = sbc.find_element(By.CLASS_NAME, 'sbc-name').text\n",
        "    sbc_list.append(sbc_name)\n",
        "\n",
        "# نمایش داده‌ها\n",
        "for sbc in sbc_list:\n",
        "    print(sbc)\n",
        "\n",
        "# بستن WebDriver\n",
        "driver.quit()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 922
        },
        "id": "XVSQbbmfIv7t",
        "outputId": "cadc07c5-55b8-4fa8-a6f0-188a8b67d53b"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: selenium in /usr/local/lib/python3.11/dist-packages (4.29.0)\n",
            "Requirement already satisfied: urllib3<3,>=1.26 in /usr/local/lib/python3.11/dist-packages (from urllib3[socks]<3,>=1.26->selenium) (2.3.0)\n",
            "Requirement already satisfied: trio~=0.17 in /usr/local/lib/python3.11/dist-packages (from selenium) (0.29.0)\n",
            "Requirement already satisfied: trio-websocket~=0.9 in /usr/local/lib/python3.11/dist-packages (from selenium) (0.12.2)\n",
            "Requirement already satisfied: certifi>=2021.10.8 in /usr/local/lib/python3.11/dist-packages (from selenium) (2025.1.31)\n",
            "Requirement already satisfied: typing_extensions~=4.9 in /usr/local/lib/python3.11/dist-packages (from selenium) (4.12.2)\n",
            "Requirement already satisfied: websocket-client~=1.8 in /usr/local/lib/python3.11/dist-packages (from selenium) (1.8.0)\n",
            "Requirement already satisfied: attrs>=23.2.0 in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (25.1.0)\n",
            "Requirement already satisfied: sortedcontainers in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (2.4.0)\n",
            "Requirement already satisfied: idna in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (3.10)\n",
            "Requirement already satisfied: outcome in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (1.3.0.post0)\n",
            "Requirement already satisfied: sniffio>=1.3.0 in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (1.3.1)\n",
            "Requirement already satisfied: wsproto>=0.14 in /usr/local/lib/python3.11/dist-packages (from trio-websocket~=0.9->selenium) (1.2.0)\n",
            "Requirement already satisfied: pysocks!=1.5.7,<2.0,>=1.5.6 in /usr/local/lib/python3.11/dist-packages (from urllib3[socks]<3,>=1.26->selenium) (1.7.1)\n",
            "Requirement already satisfied: h11<1,>=0.9.0 in /usr/local/lib/python3.11/dist-packages (from wsproto>=0.14->trio-websocket~=0.9->selenium) (0.14.0)\n",
            "Hit:1 http://archive.ubuntu.com/ubuntu jammy InRelease\n",
            "Hit:2 http://archive.ubuntu.com/ubuntu jammy-updates InRelease\n",
            "Hit:3 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64  InRelease\n",
            "Hit:4 http://archive.ubuntu.com/ubuntu jammy-backports InRelease\n",
            "Hit:5 https://cloud.r-project.org/bin/linux/ubuntu jammy-cran40/ InRelease\n",
            "Hit:6 https://r2u.stat.illinois.edu/ubuntu jammy InRelease\n",
            "Hit:7 http://security.ubuntu.com/ubuntu jammy-security InRelease\n",
            "Hit:8 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy InRelease\n",
            "Hit:9 https://ppa.launchpadcontent.net/graphics-drivers/ppa/ubuntu jammy InRelease\n",
            "Hit:10 https://ppa.launchpadcontent.net/ubuntugis/ppa/ubuntu jammy InRelease\n",
            "Reading package lists... Done\n",
            "W: Skipping acquire of configured file 'main/source/Sources' as repository 'https://r2u.stat.illinois.edu/ubuntu jammy InRelease' does not seem to provide it (sources.list entry misspelt?)\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "chromium-chromedriver is already the newest version (1:85.0.4183.83-0ubuntu2.22.04.1).\n",
            "0 upgraded, 0 newly installed, 0 to remove and 31 not upgraded.\n",
            "cp: '/usr/lib/chromium-browser/chromedriver' and '/usr/bin/chromedriver' are the same file\n",
            "Requirement already satisfied: webdriver_manager in /usr/local/lib/python3.11/dist-packages (4.0.2)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.11/dist-packages (from webdriver_manager) (2.32.3)\n",
            "Requirement already satisfied: python-dotenv in /usr/local/lib/python3.11/dist-packages (from webdriver_manager) (1.0.1)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.11/dist-packages (from webdriver_manager) (24.2)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests->webdriver_manager) (3.4.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests->webdriver_manager) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests->webdriver_manager) (2.3.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests->webdriver_manager) (2025.1.31)\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "TypeError",
          "evalue": "WebDriver.__init__() got an unexpected keyword argument 'executable_path'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-6-3a880d9d69db>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     18\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     19\u001b[0m \u001b[0;31m# راه‌اندازی WebDriver\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 20\u001b[0;31m \u001b[0mdriver\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mexecutable_path\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m'/usr/bin/chromedriver'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     21\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     22\u001b[0m \u001b[0;31m# استخراج داده‌ها از سایت\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mTypeError\u001b[0m: WebDriver.__init__() got an unexpected keyword argument 'executable_path'"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# نصب پکیج‌ها\n",
        "!pip install selenium\n",
        "!apt-get update # برای نصب وابستگی‌های Chrome\n",
        "!apt install -y chromium-chromedriver\n",
        "!cp /usr/lib/chromium-browser/chromedriver /usr/bin\n",
        "!pip install webdriver_manager\n",
        "\n",
        "# وارد کردن کتابخانه‌ها\n",
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "from selenium.webdriver.common.by import By\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from webdriver_manager.chrome import ChromeDriverManager\n",
        "\n",
        "# تنظیمات Chrome برای Colab\n",
        "options = Options()\n",
        "options.headless = True\n",
        "options.add_argument('--no-sandbox')\n",
        "options.add_argument('--disable-dev-shm-usage')\n",
        "\n",
        "# راه‌اندازی WebDriver با استفاده از Service\n",
        "service = Service(ChromeDriverManager().install())\n",
        "driver = webdriver.Chrome(service=service, options=options)\n",
        "\n",
        "# استخراج داده‌ها از سایت\n",
        "driver.get('https://www.futbin.com/squad-building-challenges')\n",
        "sbc_items = driver.find_elements(By.CLASS_NAME, 'sbc-item')\n",
        "sbc_list = []\n",
        "\n",
        "for sbc in sbc_items:\n",
        "    sbc_name = sbc.find_element(By.CLASS_NAME, 'sbc-name').text\n",
        "    sbc_list.append(sbc_name)\n",
        "\n",
        "# نمایش داده‌ها\n",
        "for sbc in sbc_list:\n",
        "    print(sbc)\n",
        "\n",
        "# بستن WebDriver\n",
        "driver.quit()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "aKyevBzCJB1y",
        "outputId": "44af3632-dfc8-4011-a02b-5d577703b1b2"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: selenium in /usr/local/lib/python3.11/dist-packages (4.29.0)\n",
            "Requirement already satisfied: urllib3<3,>=1.26 in /usr/local/lib/python3.11/dist-packages (from urllib3[socks]<3,>=1.26->selenium) (2.3.0)\n",
            "Requirement already satisfied: trio~=0.17 in /usr/local/lib/python3.11/dist-packages (from selenium) (0.29.0)\n",
            "Requirement already satisfied: trio-websocket~=0.9 in /usr/local/lib/python3.11/dist-packages (from selenium) (0.12.2)\n",
            "Requirement already satisfied: certifi>=2021.10.8 in /usr/local/lib/python3.11/dist-packages (from selenium) (2025.1.31)\n",
            "Requirement already satisfied: typing_extensions~=4.9 in /usr/local/lib/python3.11/dist-packages (from selenium) (4.12.2)\n",
            "Requirement already satisfied: websocket-client~=1.8 in /usr/local/lib/python3.11/dist-packages (from selenium) (1.8.0)\n",
            "Requirement already satisfied: attrs>=23.2.0 in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (25.1.0)\n",
            "Requirement already satisfied: sortedcontainers in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (2.4.0)\n",
            "Requirement already satisfied: idna in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (3.10)\n",
            "Requirement already satisfied: outcome in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (1.3.0.post0)\n",
            "Requirement already satisfied: sniffio>=1.3.0 in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (1.3.1)\n",
            "Requirement already satisfied: wsproto>=0.14 in /usr/local/lib/python3.11/dist-packages (from trio-websocket~=0.9->selenium) (1.2.0)\n",
            "Requirement already satisfied: pysocks!=1.5.7,<2.0,>=1.5.6 in /usr/local/lib/python3.11/dist-packages (from urllib3[socks]<3,>=1.26->selenium) (1.7.1)\n",
            "Requirement already satisfied: h11<1,>=0.9.0 in /usr/local/lib/python3.11/dist-packages (from wsproto>=0.14->trio-websocket~=0.9->selenium) (0.14.0)\n",
            "Hit:1 http://security.ubuntu.com/ubuntu jammy-security InRelease\n",
            "Hit:2 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64  InRelease\n",
            "Hit:3 https://cloud.r-project.org/bin/linux/ubuntu jammy-cran40/ InRelease\n",
            "Hit:4 https://r2u.stat.illinois.edu/ubuntu jammy InRelease\n",
            "Hit:5 http://archive.ubuntu.com/ubuntu jammy InRelease\n",
            "Hit:6 http://archive.ubuntu.com/ubuntu jammy-updates InRelease\n",
            "Hit:7 http://archive.ubuntu.com/ubuntu jammy-backports InRelease\n",
            "Hit:8 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy InRelease\n",
            "Hit:9 https://ppa.launchpadcontent.net/graphics-drivers/ppa/ubuntu jammy InRelease\n",
            "Hit:10 https://ppa.launchpadcontent.net/ubuntugis/ppa/ubuntu jammy InRelease\n",
            "Reading package lists... Done\n",
            "W: Skipping acquire of configured file 'main/source/Sources' as repository 'https://r2u.stat.illinois.edu/ubuntu jammy InRelease' does not seem to provide it (sources.list entry misspelt?)\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "chromium-chromedriver is already the newest version (1:85.0.4183.83-0ubuntu2.22.04.1).\n",
            "0 upgraded, 0 newly installed, 0 to remove and 31 not upgraded.\n",
            "cp: '/usr/lib/chromium-browser/chromedriver' and '/usr/bin/chromedriver' are the same file\n",
            "Requirement already satisfied: webdriver_manager in /usr/local/lib/python3.11/dist-packages (4.0.2)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.11/dist-packages (from webdriver_manager) (2.32.3)\n",
            "Requirement already satisfied: python-dotenv in /usr/local/lib/python3.11/dist-packages (from webdriver_manager) (1.0.1)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.11/dist-packages (from webdriver_manager) (24.2)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests->webdriver_manager) (3.4.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests->webdriver_manager) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests->webdriver_manager) (2.3.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests->webdriver_manager) (2025.1.31)\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "WebDriverException",
          "evalue": "Message: unknown error: Chrome failed to start: exited abnormally.\n  (unknown error: DevToolsActivePort file doesn't exist)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x58ccfcade4e3 <unknown>\n#1 0x58ccfc80dc76 <unknown>\n#2 0x58ccfc836d78 <unknown>\n#3 0x58ccfc833029 <unknown>\n#4 0x58ccfc871ccc <unknown>\n#5 0x58ccfc87147f <unknown>\n#6 0x58ccfc868de3 <unknown>\n#7 0x58ccfc83e2dd <unknown>\n#8 0x58ccfc83f34e <unknown>\n#9 0x58ccfca9e3e4 <unknown>\n#10 0x58ccfcaa23d7 <unknown>\n#11 0x58ccfcaacb20 <unknown>\n#12 0x58ccfcaa3023 <unknown>\n#13 0x58ccfca711aa <unknown>\n#14 0x58ccfcac76b8 <unknown>\n#15 0x58ccfcac7847 <unknown>\n#16 0x58ccfcad7243 <unknown>\n#17 0x7d10ed0cfac3 <unknown>\n",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m                        Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-7-37aa19a2b24f>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     21\u001b[0m \u001b[0;31m# راه‌اندازی WebDriver با استفاده از Service\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     22\u001b[0m \u001b[0mservice\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mService\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mChromeDriverManager\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0minstall\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 23\u001b[0;31m \u001b[0mdriver\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     24\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     25\u001b[0m \u001b[0;31m# استخراج داده‌ها از سایت\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chrome/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     43\u001b[0m         \u001b[0moptions\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0mOptions\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     44\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 45\u001b[0;31m         super().__init__(\n\u001b[0m\u001b[1;32m     46\u001b[0m             \u001b[0mbrowser_name\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mDesiredCapabilities\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCHROME\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"browserName\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     47\u001b[0m             \u001b[0mvendor_prefix\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"goog\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chromium/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, browser_name, vendor_prefix, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     64\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     65\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 66\u001b[0;31m             \u001b[0msuper\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__init__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mexecutor\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     67\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     68\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mquit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, command_executor, keep_alive, file_detector, options, locator_converter, web_element_cls, client_config)\u001b[0m\n\u001b[1;32m    248\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_authenticator_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    249\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_client\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 250\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_session\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    251\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_fedcm\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mFedCM\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    252\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mstart_session\u001b[0;34m(self, capabilities)\u001b[0m\n\u001b[1;32m    340\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    341\u001b[0m         \u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_create_caps\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 342\u001b[0;31m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mCommand\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mNEW_SESSION\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcaps\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    343\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msession_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"sessionId\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    344\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"capabilities\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, driver_command, params)\u001b[0m\n\u001b[1;32m    427\u001b[0m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    428\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 429\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    430\u001b[0m             \u001b[0mresponse\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_unwrap_value\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    431\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/errorhandler.py\u001b[0m in \u001b[0;36mcheck_response\u001b[0;34m(self, response)\u001b[0m\n\u001b[1;32m    230\u001b[0m                 \u001b[0malert_text\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"alert\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"text\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    231\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0malert_text\u001b[0m\u001b[0;34m)\u001b[0m  \u001b[0;31m# type: ignore[call-arg]  # mypy is not smart enough here\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 232\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m: Message: unknown error: Chrome failed to start: exited abnormally.\n  (unknown error: DevToolsActivePort file doesn't exist)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x58ccfcade4e3 <unknown>\n#1 0x58ccfc80dc76 <unknown>\n#2 0x58ccfc836d78 <unknown>\n#3 0x58ccfc833029 <unknown>\n#4 0x58ccfc871ccc <unknown>\n#5 0x58ccfc87147f <unknown>\n#6 0x58ccfc868de3 <unknown>\n#7 0x58ccfc83e2dd <unknown>\n#8 0x58ccfc83f34e <unknown>\n#9 0x58ccfca9e3e4 <unknown>\n#10 0x58ccfcaa23d7 <unknown>\n#11 0x58ccfcaacb20 <unknown>\n#12 0x58ccfcaa3023 <unknown>\n#13 0x58ccfca711aa <unknown>\n#14 0x58ccfcac76b8 <unknown>\n#15 0x58ccfcac7847 <unknown>\n#16 0x58ccfcad7243 <unknown>\n#17 0x7d10ed0cfac3 <unknown>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# نصب پکیج‌ها\n",
        "!pip install selenium\n",
        "!apt-get update # برای نصب وابستگی‌های Chrome\n",
        "!apt install -y chromium-chromedriver\n",
        "!cp /usr/lib/chromium-browser/chromedriver /usr/bin\n",
        "!pip install webdriver_manager\n",
        "\n",
        "# وارد کردن کتابخانه‌ها\n",
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from webdriver_manager.chrome import ChromeDriverManager\n",
        "from selenium.webdriver.common.by import By\n",
        "\n",
        "# تنظیمات Chrome برای Colab\n",
        "options = Options()\n",
        "options.add_argument('--headless')  # اجرای Chrome در حالت headless\n",
        "options.add_argument('--no-sandbox')\n",
        "options.add_argument('--disable-dev-shm-usage')\n",
        "options.add_argument('--remote-debugging-port=9222')  # جلوگیری از کرش\n",
        "options.add_argument(\"--disable-gpu\")  # برخی مشکلات مربوط به گرافیک را حل می‌کند\n",
        "options.binary_location = \"/usr/bin/chromium-browser\"  # مشخص کردن مسیر کروم\n",
        "\n",
        "# راه‌اندازی WebDriver با استفاده از Service\n",
        "service = Service(\"/usr/bin/chromedriver\")  # مشخص کردن مسیر chromedriver\n",
        "driver = webdriver.Chrome(service=service, options=options)\n",
        "\n",
        "# استخراج داده‌ها از سایت\n",
        "driver.get('https://www.futbin.com/squad-building-challenges')\n",
        "\n",
        "# تلاش برای یافتن عناصر (بررسی کنید که کلاس درست باشد)\n",
        "sbc_items = driver.find_elements(By.CLASS_NAME, 'sbc-item')\n",
        "sbc_list = []\n",
        "\n",
        "for sbc in sbc_items:\n",
        "    sbc_name = sbc.find_element(By.CLASS_NAME, 'sbc-name').text\n",
        "    sbc_list.append(sbc_name)\n",
        "\n",
        "# نمایش داده‌ها\n",
        "for sbc in sbc_list:\n",
        "    print(sbc)\n",
        "\n",
        "# بستن WebDriver\n",
        "driver.quit()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "QQ0rNvwlJU5S",
        "outputId": "f869117c-883f-49b1-f756-dc870e7ffdf6"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: selenium in /usr/local/lib/python3.11/dist-packages (4.29.0)\n",
            "Requirement already satisfied: urllib3<3,>=1.26 in /usr/local/lib/python3.11/dist-packages (from urllib3[socks]<3,>=1.26->selenium) (2.3.0)\n",
            "Requirement already satisfied: trio~=0.17 in /usr/local/lib/python3.11/dist-packages (from selenium) (0.29.0)\n",
            "Requirement already satisfied: trio-websocket~=0.9 in /usr/local/lib/python3.11/dist-packages (from selenium) (0.12.2)\n",
            "Requirement already satisfied: certifi>=2021.10.8 in /usr/local/lib/python3.11/dist-packages (from selenium) (2025.1.31)\n",
            "Requirement already satisfied: typing_extensions~=4.9 in /usr/local/lib/python3.11/dist-packages (from selenium) (4.12.2)\n",
            "Requirement already satisfied: websocket-client~=1.8 in /usr/local/lib/python3.11/dist-packages (from selenium) (1.8.0)\n",
            "Requirement already satisfied: attrs>=23.2.0 in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (25.1.0)\n",
            "Requirement already satisfied: sortedcontainers in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (2.4.0)\n",
            "Requirement already satisfied: idna in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (3.10)\n",
            "Requirement already satisfied: outcome in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (1.3.0.post0)\n",
            "Requirement already satisfied: sniffio>=1.3.0 in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (1.3.1)\n",
            "Requirement already satisfied: wsproto>=0.14 in /usr/local/lib/python3.11/dist-packages (from trio-websocket~=0.9->selenium) (1.2.0)\n",
            "Requirement already satisfied: pysocks!=1.5.7,<2.0,>=1.5.6 in /usr/local/lib/python3.11/dist-packages (from urllib3[socks]<3,>=1.26->selenium) (1.7.1)\n",
            "Requirement already satisfied: h11<1,>=0.9.0 in /usr/local/lib/python3.11/dist-packages (from wsproto>=0.14->trio-websocket~=0.9->selenium) (0.14.0)\n",
            "Hit:1 http://archive.ubuntu.com/ubuntu jammy InRelease\n",
            "Hit:2 https://cloud.r-project.org/bin/linux/ubuntu jammy-cran40/ InRelease\n",
            "Hit:3 http://archive.ubuntu.com/ubuntu jammy-updates InRelease\n",
            "Hit:4 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64  InRelease\n",
            "Hit:5 http://archive.ubuntu.com/ubuntu jammy-backports InRelease\n",
            "Hit:6 https://r2u.stat.illinois.edu/ubuntu jammy InRelease\n",
            "Hit:7 http://security.ubuntu.com/ubuntu jammy-security InRelease\n",
            "Hit:8 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy InRelease\n",
            "Hit:9 https://ppa.launchpadcontent.net/graphics-drivers/ppa/ubuntu jammy InRelease\n",
            "Hit:10 https://ppa.launchpadcontent.net/ubuntugis/ppa/ubuntu jammy InRelease\n",
            "Reading package lists... Done\n",
            "W: Skipping acquire of configured file 'main/source/Sources' as repository 'https://r2u.stat.illinois.edu/ubuntu jammy InRelease' does not seem to provide it (sources.list entry misspelt?)\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "chromium-chromedriver is already the newest version (1:85.0.4183.83-0ubuntu2.22.04.1).\n",
            "0 upgraded, 0 newly installed, 0 to remove and 31 not upgraded.\n",
            "cp: '/usr/lib/chromium-browser/chromedriver' and '/usr/bin/chromedriver' are the same file\n",
            "Requirement already satisfied: webdriver_manager in /usr/local/lib/python3.11/dist-packages (4.0.2)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.11/dist-packages (from webdriver_manager) (2.32.3)\n",
            "Requirement already satisfied: python-dotenv in /usr/local/lib/python3.11/dist-packages (from webdriver_manager) (1.0.1)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.11/dist-packages (from webdriver_manager) (24.2)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests->webdriver_manager) (3.4.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests->webdriver_manager) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests->webdriver_manager) (2.3.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests->webdriver_manager) (2025.1.31)\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "WebDriverException",
          "evalue": "Message: Service /usr/bin/chromedriver unexpectedly exited. Status code was: 1\n",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m                        Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-8-8ba305b932e7>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     24\u001b[0m \u001b[0;31m# راه‌اندازی WebDriver با استفاده از Service\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     25\u001b[0m \u001b[0mservice\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mService\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"/usr/bin/chromedriver\"\u001b[0m\u001b[0;34m)\u001b[0m  \u001b[0;31m# مشخص کردن مسیر chromedriver\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 26\u001b[0;31m \u001b[0mdriver\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     27\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     28\u001b[0m \u001b[0;31m# استخراج داده‌ها از سایت\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chrome/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     43\u001b[0m         \u001b[0moptions\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0mOptions\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     44\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 45\u001b[0;31m         super().__init__(\n\u001b[0m\u001b[1;32m     46\u001b[0m             \u001b[0mbrowser_name\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mDesiredCapabilities\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCHROME\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"browserName\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     47\u001b[0m             \u001b[0mvendor_prefix\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"goog\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chromium/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, browser_name, vendor_prefix, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     53\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     54\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpath\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0menv_path\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0mfinder\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_driver_path\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 55\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     56\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     57\u001b[0m         executor = ChromiumRemoteConnection(\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/common/service.py\u001b[0m in \u001b[0;36mstart\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    111\u001b[0m         \u001b[0mcount\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    112\u001b[0m         \u001b[0;32mwhile\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 113\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0massert_process_still_running\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    114\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mis_connectable\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    115\u001b[0m                 \u001b[0;32mbreak\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/common/service.py\u001b[0m in \u001b[0;36massert_process_still_running\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    124\u001b[0m         \u001b[0mreturn_code\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mprocess\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpoll\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    125\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mreturn_code\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 126\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mWebDriverException\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mf\"Service {self._path} unexpectedly exited. Status code was: {return_code}\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    127\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    128\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mis_connectable\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m->\u001b[0m \u001b[0mbool\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mWebDriverException\u001b[0m: Message: Service /usr/bin/chromedriver unexpectedly exited. Status code was: 1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!which google-chrome\n",
        "!which chromium-browser\n",
        "!which chromedriver\n",
        "!google-chrome --version\n",
        "!chromedriver --version\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "m4qnikV-Jkox",
        "outputId": "f5c94ab6-2c62-4682-f162-631b99737980"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/usr/bin/chromium-browser\n",
            "/usr/bin/chromedriver\n",
            "/bin/bash: line 1: google-chrome: command not found\n",
            "\n",
            "Command '/usr/bin/chromedriver' requires the chromium snap to be installed.\n",
            "Please install it with:\n",
            "\n",
            "snap install chromium\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!apt-get purge google-chrome-stable chromium-browser chromedriver -y\n",
        "!apt-get autoremove -y\n",
        "!apt-get update\n",
        "!apt-get install -y chromium-browser chromium-chromedriver\n",
        "!cp /usr/lib/chromium-browser/chromedriver /usr/bin/chromedriver\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_92wSHTzJqkI",
        "outputId": "80a53a0f-47bb-4608-9691-d4827650cccc"
      },
      "execution_count": 10,
      "outputs": [
        {
          "metadata": {
            "tags": null
          },
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "Package 'chromedriver' is not installed, so not removed\n",
            "E: Unable to locate package google-chrome-stable\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "0 upgraded, 0 newly installed, 0 to remove and 31 not upgraded.\n",
            "Hit:1 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64  InRelease\n",
            "Hit:2 http://archive.ubuntu.com/ubuntu jammy InRelease\n",
            "Hit:3 https://cloud.r-project.org/bin/linux/ubuntu jammy-cran40/ InRelease\n",
            "Hit:4 http://archive.ubuntu.com/ubuntu jammy-updates InRelease\n",
            "Hit:5 http://archive.ubuntu.com/ubuntu jammy-backports InRelease\n",
            "Hit:6 https://r2u.stat.illinois.edu/ubuntu jammy InRelease\n",
            "Hit:7 http://security.ubuntu.com/ubuntu jammy-security InRelease\n",
            "Hit:8 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy InRelease\n",
            "Hit:9 https://ppa.launchpadcontent.net/graphics-drivers/ppa/ubuntu jammy InRelease\n",
            "Hit:10 https://ppa.launchpadcontent.net/ubuntugis/ppa/ubuntu jammy InRelease\n",
            "Reading package lists... Done\n",
            "W: Skipping acquire of configured file 'main/source/Sources' as repository 'https://r2u.stat.illinois.edu/ubuntu jammy InRelease' does not seem to provide it (sources.list entry misspelt?)\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "chromium-browser is already the newest version (1:85.0.4183.83-0ubuntu2.22.04.1).\n",
            "chromium-browser set to manually installed.\n",
            "chromium-chromedriver is already the newest version (1:85.0.4183.83-0ubuntu2.22.04.1).\n",
            "0 upgraded, 0 newly installed, 0 to remove and 31 not upgraded.\n",
            "cp: '/usr/lib/chromium-browser/chromedriver' and '/usr/bin/chromedriver' are the same file\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!which chromedriver\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Zjn0_R4dJvdf",
        "outputId": "e7d81f3c-f9b8-4040-8a05-3c7034f81384"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/usr/bin/chromedriver\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "Mo3ZlKaYKmwO"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install selenium webdriver_manager\n",
        "\n",
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "from webdriver_manager.chrome import ChromeDriverManager\n",
        "\n",
        "options = Options()\n",
        "options.add_argument('--headless')\n",
        "options.add_argument('--no-sandbox')\n",
        "options.add_argument('--disable-dev-shm-usage')\n",
        "\n",
        "# استفاده از webdriver_manager برای دانلود و راه‌اندازی درایور\n",
        "service = Service(ChromeDriverManager().install())\n",
        "driver = webdriver.Chrome(service=service, options=options)\n",
        "\n",
        "driver.get(\"https://www.google.com\")\n",
        "print(\"Chrome WebDriver اجرا شد!\")\n",
        "driver.quit()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "U9GgBs2vJzF7",
        "outputId": "cfc53e8d-d8e8-403e-ad76-e682f939e4bc"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: selenium in /usr/local/lib/python3.11/dist-packages (4.29.0)\n",
            "Requirement already satisfied: webdriver_manager in /usr/local/lib/python3.11/dist-packages (4.0.2)\n",
            "Requirement already satisfied: urllib3<3,>=1.26 in /usr/local/lib/python3.11/dist-packages (from urllib3[socks]<3,>=1.26->selenium) (2.3.0)\n",
            "Requirement already satisfied: trio~=0.17 in /usr/local/lib/python3.11/dist-packages (from selenium) (0.29.0)\n",
            "Requirement already satisfied: trio-websocket~=0.9 in /usr/local/lib/python3.11/dist-packages (from selenium) (0.12.2)\n",
            "Requirement already satisfied: certifi>=2021.10.8 in /usr/local/lib/python3.11/dist-packages (from selenium) (2025.1.31)\n",
            "Requirement already satisfied: typing_extensions~=4.9 in /usr/local/lib/python3.11/dist-packages (from selenium) (4.12.2)\n",
            "Requirement already satisfied: websocket-client~=1.8 in /usr/local/lib/python3.11/dist-packages (from selenium) (1.8.0)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.11/dist-packages (from webdriver_manager) (2.32.3)\n",
            "Requirement already satisfied: python-dotenv in /usr/local/lib/python3.11/dist-packages (from webdriver_manager) (1.0.1)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.11/dist-packages (from webdriver_manager) (24.2)\n",
            "Requirement already satisfied: attrs>=23.2.0 in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (25.1.0)\n",
            "Requirement already satisfied: sortedcontainers in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (2.4.0)\n",
            "Requirement already satisfied: idna in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (3.10)\n",
            "Requirement already satisfied: outcome in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (1.3.0.post0)\n",
            "Requirement already satisfied: sniffio>=1.3.0 in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (1.3.1)\n",
            "Requirement already satisfied: wsproto>=0.14 in /usr/local/lib/python3.11/dist-packages (from trio-websocket~=0.9->selenium) (1.2.0)\n",
            "Requirement already satisfied: pysocks!=1.5.7,<2.0,>=1.5.6 in /usr/local/lib/python3.11/dist-packages (from urllib3[socks]<3,>=1.26->selenium) (1.7.1)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests->webdriver_manager) (3.4.1)\n",
            "Requirement already satisfied: h11<1,>=0.9.0 in /usr/local/lib/python3.11/dist-packages (from wsproto>=0.14->trio-websocket~=0.9->selenium) (0.14.0)\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "WebDriverException",
          "evalue": "Message: unknown error: Chrome failed to start: exited abnormally.\n  (unknown error: DevToolsActivePort file doesn't exist)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x5bc41478f4e3 <unknown>\n#1 0x5bc4144bec76 <unknown>\n#2 0x5bc4144e7d78 <unknown>\n#3 0x5bc4144e4029 <unknown>\n#4 0x5bc414522ccc <unknown>\n#5 0x5bc41452247f <unknown>\n#6 0x5bc414519de3 <unknown>\n#7 0x5bc4144ef2dd <unknown>\n#8 0x5bc4144f034e <unknown>\n#9 0x5bc41474f3e4 <unknown>\n#10 0x5bc4147533d7 <unknown>\n#11 0x5bc41475db20 <unknown>\n#12 0x5bc414754023 <unknown>\n#13 0x5bc4147221aa <unknown>\n#14 0x5bc4147786b8 <unknown>\n#15 0x5bc414778847 <unknown>\n#16 0x5bc414788243 <unknown>\n#17 0x7efd199c4ac3 <unknown>\n",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m                        Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-12-dcb15248b0cc>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     13\u001b[0m \u001b[0;31m# استفاده از webdriver_manager برای دانلود و راه‌اندازی درایور\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     14\u001b[0m \u001b[0mservice\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mService\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mChromeDriverManager\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0minstall\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 15\u001b[0;31m \u001b[0mdriver\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     16\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     17\u001b[0m \u001b[0mdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"https://www.google.com\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chrome/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     43\u001b[0m         \u001b[0moptions\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0mOptions\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     44\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 45\u001b[0;31m         super().__init__(\n\u001b[0m\u001b[1;32m     46\u001b[0m             \u001b[0mbrowser_name\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mDesiredCapabilities\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCHROME\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"browserName\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     47\u001b[0m             \u001b[0mvendor_prefix\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"goog\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chromium/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, browser_name, vendor_prefix, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     64\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     65\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 66\u001b[0;31m             \u001b[0msuper\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__init__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mexecutor\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     67\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     68\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mquit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, command_executor, keep_alive, file_detector, options, locator_converter, web_element_cls, client_config)\u001b[0m\n\u001b[1;32m    248\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_authenticator_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    249\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_client\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 250\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_session\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    251\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_fedcm\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mFedCM\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    252\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mstart_session\u001b[0;34m(self, capabilities)\u001b[0m\n\u001b[1;32m    340\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    341\u001b[0m         \u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_create_caps\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 342\u001b[0;31m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mCommand\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mNEW_SESSION\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcaps\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    343\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msession_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"sessionId\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    344\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"capabilities\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, driver_command, params)\u001b[0m\n\u001b[1;32m    427\u001b[0m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    428\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 429\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    430\u001b[0m             \u001b[0mresponse\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_unwrap_value\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    431\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/errorhandler.py\u001b[0m in \u001b[0;36mcheck_response\u001b[0;34m(self, response)\u001b[0m\n\u001b[1;32m    230\u001b[0m                 \u001b[0malert_text\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"alert\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"text\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    231\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0malert_text\u001b[0m\u001b[0;34m)\u001b[0m  \u001b[0;31m# type: ignore[call-arg]  # mypy is not smart enough here\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 232\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m: Message: unknown error: Chrome failed to start: exited abnormally.\n  (unknown error: DevToolsActivePort file doesn't exist)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x5bc41478f4e3 <unknown>\n#1 0x5bc4144bec76 <unknown>\n#2 0x5bc4144e7d78 <unknown>\n#3 0x5bc4144e4029 <unknown>\n#4 0x5bc414522ccc <unknown>\n#5 0x5bc41452247f <unknown>\n#6 0x5bc414519de3 <unknown>\n#7 0x5bc4144ef2dd <unknown>\n#8 0x5bc4144f034e <unknown>\n#9 0x5bc41474f3e4 <unknown>\n#10 0x5bc4147533d7 <unknown>\n#11 0x5bc41475db20 <unknown>\n#12 0x5bc414754023 <unknown>\n#13 0x5bc4147221aa <unknown>\n#14 0x5bc4147786b8 <unknown>\n#15 0x5bc414778847 <unknown>\n#16 0x5bc414788243 <unknown>\n#17 0x7efd199c4ac3 <unknown>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb\n",
        "!dpkg -i google-chrome-stable_current_amd64.deb\n",
        "!apt-get -f install -y\n",
        "!google-chrome --version\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZDxF0DroJ73N",
        "outputId": "9ee7bde3-1056-425e-e56c-7bf0a0c4a043"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "--2025-03-11 07:42:29--  https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb\n",
            "Resolving dl.google.com (dl.google.com)... 209.85.200.93, 209.85.200.136, 209.85.200.190, ...\n",
            "Connecting to dl.google.com (dl.google.com)|209.85.200.93|:443... connected.\n",
            "HTTP request sent, awaiting response... 200 OK\n",
            "Length: 114745904 (109M) [application/x-debian-package]\n",
            "Saving to: ‘google-chrome-stable_current_amd64.deb’\n",
            "\n",
            "google-chrome-stabl 100%[===================>] 109.43M   320MB/s    in 0.3s    \n",
            "\n",
            "2025-03-11 07:42:30 (320 MB/s) - ‘google-chrome-stable_current_amd64.deb’ saved [114745904/114745904]\n",
            "\n",
            "Selecting previously unselected package google-chrome-stable.\n",
            "(Reading database ... 125412 files and directories currently installed.)\n",
            "Preparing to unpack google-chrome-stable_current_amd64.deb ...\n",
            "Unpacking google-chrome-stable (134.0.6998.88-1) ...\n",
            "\u001b[1mdpkg:\u001b[0m dependency problems prevent configuration of google-chrome-stable:\n",
            " google-chrome-stable depends on libvulkan1; however:\n",
            "  Package libvulkan1 is not installed.\n",
            "\n",
            "\u001b[1mdpkg:\u001b[0m error processing package google-chrome-stable (--install):\n",
            " dependency problems - leaving unconfigured\n",
            "Processing triggers for mailcap (3.70+nmu1ubuntu1) ...\n",
            "Processing triggers for man-db (2.10.2-1) ...\n",
            "Errors were encountered while processing:\n",
            " google-chrome-stable\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "Correcting dependencies... Done\n",
            "The following additional packages will be installed:\n",
            "  libvulkan1 mesa-vulkan-drivers\n",
            "The following NEW packages will be installed:\n",
            "  libvulkan1 mesa-vulkan-drivers\n",
            "0 upgraded, 2 newly installed, 0 to remove and 31 not upgraded.\n",
            "1 not fully installed or removed.\n",
            "Need to get 10.9 MB of archives.\n",
            "After this operation, 51.3 MB of additional disk space will be used.\n",
            "Get:1 http://archive.ubuntu.com/ubuntu jammy/main amd64 libvulkan1 amd64 1.3.204.1-2 [128 kB]\n",
            "Get:2 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 mesa-vulkan-drivers amd64 23.2.1-1ubuntu3.1~22.04.3 [10.7 MB]\n",
            "Fetched 10.9 MB in 1s (18.8 MB/s)\n",
            "Selecting previously unselected package libvulkan1:amd64.\n",
            "(Reading database ... 125529 files and directories currently installed.)\n",
            "Preparing to unpack .../libvulkan1_1.3.204.1-2_amd64.deb ...\n",
            "Unpacking libvulkan1:amd64 (1.3.204.1-2) ...\n",
            "Selecting previously unselected package mesa-vulkan-drivers:amd64.\n",
            "Preparing to unpack .../mesa-vulkan-drivers_23.2.1-1ubuntu3.1~22.04.3_amd64.deb ...\n",
            "Unpacking mesa-vulkan-drivers:amd64 (23.2.1-1ubuntu3.1~22.04.3) ...\n",
            "Setting up libvulkan1:amd64 (1.3.204.1-2) ...\n",
            "Setting up mesa-vulkan-drivers:amd64 (23.2.1-1ubuntu3.1~22.04.3) ...\n",
            "Setting up google-chrome-stable (134.0.6998.88-1) ...\n",
            "update-alternatives: using /usr/bin/google-chrome-stable to provide /usr/bin/x-www-browser (x-www-browser) in auto mode\n",
            "update-alternatives: using /usr/bin/google-chrome-stable to provide /usr/bin/gnome-www-browser (gnome-www-browser) in auto mode\n",
            "update-alternatives: using /usr/bin/google-chrome-stable to provide /usr/bin/google-chrome (google-chrome) in auto mode\n",
            "Processing triggers for libc-bin (2.35-0ubuntu3.8) ...\n",
            "/sbin/ldconfig.real: /usr/local/lib/libur_adapter_level_zero.so.0 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtbbmalloc.so.2 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libhwloc.so.15 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtcm.so.1 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtbb.so.12 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtbbbind_2_5.so.3 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libur_adapter_opencl.so.0 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtbbmalloc_proxy.so.2 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libur_loader.so.0 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libumf.so.0 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtbbbind_2_0.so.3 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtbbbind.so.3 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtcm_debug.so.1 is not a symbolic link\n",
            "\n",
            "Google Chrome 134.0.6998.88 \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!which google-chrome\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vUcQ142qKCmB",
        "outputId": "0ae9345a-effa-4231-9f24-3b8c2ef93c4d"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/usr/bin/google-chrome\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!sudo apt-get remove --purge google-chrome-stable -y\n",
        "!sudo apt-get remove --purge chromium-browser -y\n",
        "!sudo apt-get autoremove -y\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "w6fCwFBOKRCL",
        "outputId": "3bdade00-9a0e-4d27-9c75-8b4a3ce292c7"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "The following packages were automatically installed and are no longer required:\n",
            "  libvulkan1 mesa-vulkan-drivers\n",
            "Use 'sudo apt autoremove' to remove them.\n",
            "The following packages will be REMOVED:\n",
            "  google-chrome-stable*\n",
            "0 upgraded, 0 newly installed, 1 to remove and 31 not upgraded.\n",
            "After this operation, 375 MB disk space will be freed.\n",
            "(Reading database ... 125567 files and directories currently installed.)\n",
            "Removing google-chrome-stable (134.0.6998.88-1) ...\n",
            "update-alternatives: using /usr/bin/chromium-browser to provide /usr/bin/x-www-browser (x-www-browser) in auto mode\n",
            "update-alternatives: using /usr/bin/chromium-browser to provide /usr/bin/gnome-www-browser (gnome-www-browser) in auto mode\n",
            "Processing triggers for mailcap (3.70+nmu1ubuntu1) ...\n",
            "Processing triggers for man-db (2.10.2-1) ...\n",
            "(Reading database ... 125451 files and directories currently installed.)\n",
            "Purging configuration files for google-chrome-stable (134.0.6998.88-1) ...\n",
            "dpkg: warning: while removing google-chrome-stable, directory '/opt/google' not empty so not removed\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "The following packages were automatically installed and are no longer required:\n",
            "  apparmor libfuse3-3 liblzo2-2 libvulkan1 mesa-vulkan-drivers snapd\n",
            "  squashfs-tools systemd-hwe-hwdb udev\n",
            "Use 'sudo apt autoremove' to remove them.\n",
            "The following packages will be REMOVED:\n",
            "  chromium-browser* chromium-chromedriver*\n",
            "0 upgraded, 0 newly installed, 2 to remove and 31 not upgraded.\n",
            "After this operation, 243 kB disk space will be freed.\n",
            "(Reading database ... 125450 files and directories currently installed.)\n",
            "Removing chromium-chromedriver (1:85.0.4183.83-0ubuntu2.22.04.1) ...\n",
            "Removing chromium-browser (1:85.0.4183.83-0ubuntu2.22.04.1) ...\n",
            "Processing triggers for mailcap (3.70+nmu1ubuntu1) ...\n",
            "Processing triggers for hicolor-icon-theme (0.17-2) ...\n",
            "(Reading database ... 125429 files and directories currently installed.)\n",
            "Purging configuration files for chromium-browser (1:85.0.4183.83-0ubuntu2.22.04.1) ...\n",
            "debconf: unable to initialize frontend: Dialog\n",
            "debconf: (No usable dialog-like program is installed, so the dialog based frontend cannot be used. at /usr/share/perl5/Debconf/FrontEnd/Dialog.pm line 78.)\n",
            "debconf: falling back to frontend: Readline\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "The following packages will be REMOVED:\n",
            "  apparmor libfuse3-3 liblzo2-2 libvulkan1 mesa-vulkan-drivers snapd\n",
            "  squashfs-tools systemd-hwe-hwdb udev\n",
            "0 upgraded, 0 newly installed, 9 to remove and 31 not upgraded.\n",
            "After this operation, 174 MB disk space will be freed.\n",
            "(Reading database ... 125429 files and directories currently installed.)\n",
            "Removing snapd (2.67.1+22.04) ...\n",
            "Removing apparmor (3.0.4-2ubuntu2.4) ...\n",
            "Removing libfuse3-3:amd64 (3.10.5-1build1) ...\n",
            "Removing squashfs-tools (1:4.5-3build1) ...\n",
            "Removing liblzo2-2:amd64 (2.10-2build3) ...\n",
            "Removing mesa-vulkan-drivers:amd64 (23.2.1-1ubuntu3.1~22.04.3) ...\n",
            "Removing libvulkan1:amd64 (1.3.204.1-2) ...\n",
            "Removing systemd-hwe-hwdb (249.11.5) ...\n",
            "Removing udev (249.11-0ubuntu3.12) ...\n",
            "invoke-rc.d: could not determine current runlevel\n",
            "invoke-rc.d: policy-rc.d denied execution of stop.\n",
            "Processing triggers for man-db (2.10.2-1) ...\n",
            "Processing triggers for dbus (1.12.20-2ubuntu4.1) ...\n",
            "Processing triggers for mailcap (3.70+nmu1ubuntu1) ...\n",
            "Processing triggers for libc-bin (2.35-0ubuntu3.8) ...\n",
            "/sbin/ldconfig.real: /usr/local/lib/libur_adapter_level_zero.so.0 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtbbmalloc.so.2 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libhwloc.so.15 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtcm.so.1 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtbb.so.12 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtbbbind_2_5.so.3 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libur_adapter_opencl.so.0 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtbbmalloc_proxy.so.2 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libur_loader.so.0 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libumf.so.0 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtbbbind_2_0.so.3 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtbbbind.so.3 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtcm_debug.so.1 is not a symbolic link\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb\n",
        "!sudo dpkg -i google-chrome-stable_current_amd64.deb || sudo apt-get -f install -y\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Vf39-UVvKWO3",
        "outputId": "a267aa4d-137d-4629-b85e-03df2285221c"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "--2025-03-11 07:44:17--  https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb\n",
            "Resolving dl.google.com (dl.google.com)... 142.250.125.136, 142.250.125.93, 142.250.125.190, ...\n",
            "Connecting to dl.google.com (dl.google.com)|142.250.125.136|:443... connected.\n",
            "HTTP request sent, awaiting response... 200 OK\n",
            "Length: 114745904 (109M) [application/x-debian-package]\n",
            "Saving to: ‘google-chrome-stable_current_amd64.deb.1’\n",
            "\n",
            "google-chrome-stabl 100%[===================>] 109.43M   312MB/s    in 0.4s    \n",
            "\n",
            "2025-03-11 07:44:17 (312 MB/s) - ‘google-chrome-stable_current_amd64.deb.1’ saved [114745904/114745904]\n",
            "\n",
            "Selecting previously unselected package google-chrome-stable.\n",
            "(Reading database ... 125113 files and directories currently installed.)\n",
            "Preparing to unpack google-chrome-stable_current_amd64.deb ...\n",
            "Unpacking google-chrome-stable (134.0.6998.88-1) ...\n",
            "\u001b[1mdpkg:\u001b[0m dependency problems prevent configuration of google-chrome-stable:\n",
            " google-chrome-stable depends on libvulkan1; however:\n",
            "  Package libvulkan1 is not installed.\n",
            "\n",
            "\u001b[1mdpkg:\u001b[0m error processing package google-chrome-stable (--install):\n",
            " dependency problems - leaving unconfigured\n",
            "Processing triggers for mailcap (3.70+nmu1ubuntu1) ...\n",
            "Processing triggers for man-db (2.10.2-1) ...\n",
            "Errors were encountered while processing:\n",
            " google-chrome-stable\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "Correcting dependencies... Done\n",
            "The following additional packages will be installed:\n",
            "  libvulkan1 mesa-vulkan-drivers\n",
            "The following NEW packages will be installed:\n",
            "  libvulkan1 mesa-vulkan-drivers\n",
            "0 upgraded, 2 newly installed, 0 to remove and 31 not upgraded.\n",
            "1 not fully installed or removed.\n",
            "Need to get 10.9 MB of archives.\n",
            "After this operation, 51.3 MB of additional disk space will be used.\n",
            "Get:1 http://archive.ubuntu.com/ubuntu jammy/main amd64 libvulkan1 amd64 1.3.204.1-2 [128 kB]\n",
            "Get:2 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 mesa-vulkan-drivers amd64 23.2.1-1ubuntu3.1~22.04.3 [10.7 MB]\n",
            "Fetched 10.9 MB in 1s (7,285 kB/s)\n",
            "debconf: unable to initialize frontend: Dialog\n",
            "debconf: (No usable dialog-like program is installed, so the dialog based frontend cannot be used. at /usr/share/perl5/Debconf/FrontEnd/Dialog.pm line 78, <> line 2.)\n",
            "debconf: falling back to frontend: Readline\n",
            "debconf: unable to initialize frontend: Readline\n",
            "debconf: (This frontend requires a controlling tty.)\n",
            "debconf: falling back to frontend: Teletype\n",
            "dpkg-preconfigure: unable to re-open stdin: \n",
            "Selecting previously unselected package libvulkan1:amd64.\n",
            "(Reading database ... 125230 files and directories currently installed.)\n",
            "Preparing to unpack .../libvulkan1_1.3.204.1-2_amd64.deb ...\n",
            "Unpacking libvulkan1:amd64 (1.3.204.1-2) ...\n",
            "Selecting previously unselected package mesa-vulkan-drivers:amd64.\n",
            "Preparing to unpack .../mesa-vulkan-drivers_23.2.1-1ubuntu3.1~22.04.3_amd64.deb ...\n",
            "Unpacking mesa-vulkan-drivers:amd64 (23.2.1-1ubuntu3.1~22.04.3) ...\n",
            "Setting up libvulkan1:amd64 (1.3.204.1-2) ...\n",
            "Setting up mesa-vulkan-drivers:amd64 (23.2.1-1ubuntu3.1~22.04.3) ...\n",
            "Setting up google-chrome-stable (134.0.6998.88-1) ...\n",
            "update-alternatives: using /usr/bin/google-chrome-stable to provide /usr/bin/x-www-browser (x-www-browser) in auto mode\n",
            "update-alternatives: using /usr/bin/google-chrome-stable to provide /usr/bin/gnome-www-browser (gnome-www-browser) in auto mode\n",
            "update-alternatives: using /usr/bin/google-chrome-stable to provide /usr/bin/google-chrome (google-chrome) in auto mode\n",
            "Processing triggers for libc-bin (2.35-0ubuntu3.8) ...\n",
            "/sbin/ldconfig.real: /usr/local/lib/libur_adapter_level_zero.so.0 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtbbmalloc.so.2 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libhwloc.so.15 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtcm.so.1 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtbb.so.12 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtbbbind_2_5.so.3 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libur_adapter_opencl.so.0 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtbbmalloc_proxy.so.2 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libur_loader.so.0 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libumf.so.0 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtbbbind_2_0.so.3 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtbbbind.so.3 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtcm_debug.so.1 is not a symbolic link\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "qnaCBJ6tKv_Y"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!which chromedriver\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "e7d81f3c-f9b8-4040-8a05-3c7034f81384",
        "id": "iwF5zSKOKwRL"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/usr/bin/chromedriver\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!google-chrome --version\n",
        "!chromedriver --version\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xMvjqvAGLIdR",
        "outputId": "5badad53-d1f0-41a0-a010-a73258361fb1"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Google Chrome 134.0.6998.88 \n",
            "/bin/bash: line 1: chromedriver: command not found\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!wget https://storage.googleapis.com/chrome-for-testing-public/134.0.6998.88/linux64/chromedriver-linux64.zip\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rUdAvuwTLQfS",
        "outputId": "d60bfdc1-87b4-4ef7-e749-b3f6065168dc"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "--2025-03-11 07:48:16--  https://storage.googleapis.com/chrome-for-testing-public/134.0.6998.88/linux64/chromedriver-linux64.zip\n",
            "Resolving storage.googleapis.com (storage.googleapis.com)... 64.233.179.207, 108.177.121.207, 209.85.145.207, ...\n",
            "Connecting to storage.googleapis.com (storage.googleapis.com)|64.233.179.207|:443... connected.\n",
            "HTTP request sent, awaiting response... 200 OK\n",
            "Length: 9521717 (9.1M) [application/zip]\n",
            "Saving to: ‘chromedriver-linux64.zip’\n",
            "\n",
            "\rchromedriver-linux6   0%[                    ]       0  --.-KB/s               \rchromedriver-linux6 100%[===================>]   9.08M  --.-KB/s    in 0.06s   \n",
            "\n",
            "2025-03-11 07:48:16 (162 MB/s) - ‘chromedriver-linux64.zip’ saved [9521717/9521717]\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!unzip chromedriver-linux64.zip\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1CZVTj_5LSzO",
        "outputId": "63f341ce-1583-48c8-e850-cf3a1c27bd6b"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Archive:  chromedriver-linux64.zip\n",
            "  inflating: chromedriver-linux64/LICENSE.chromedriver  \n",
            "  inflating: chromedriver-linux64/THIRD_PARTY_NOTICES.chromedriver  \n",
            "  inflating: chromedriver-linux64/chromedriver  \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!sudo mv chromedriver-linux64/chromedriver /usr/bin/chromedriver\n",
        "!sudo chmod +x /usr/bin/chromedriver\n"
      ],
      "metadata": {
        "id": "Y5Kb-gp2LVCy"
      },
      "execution_count": 22,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!chromedriver --version\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "a4Yt19uzLXJx",
        "outputId": "a7630040-9a34-4953-df82-f42f1fbebef4"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "ChromeDriver 134.0.6998.88 (7e3d5c978c6d3a6eda25692cfac7f893a2b20dd0-refs/branch-heads/6998@{#1898})\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "\n",
        "options = Options()\n",
        "options.add_argument('--headless')  # بدون رابط گرافیکی\n",
        "options.add_argument('--no-sandbox')\n",
        "options.add_argument('--disable-dev-shm-usage')\n",
        "\n",
        "service = Service(\"/usr/bin/chromedriver\")\n",
        "driver = webdriver.Chrome(service=service, options=options)\n",
        "\n",
        "driver.get(\"https://www.google.com\")\n",
        "print(\"کروم با موفقیت اجرا شد!\")\n",
        "driver.quit()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bfYtYg4QLb-D",
        "outputId": "641fafb9-e46d-440d-e7a5-91d1b2c8f492"
      },
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "کروم با موفقیت اجرا شد!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "\n",
        "# تنظیمات کروم برای اجرا در حالت headless\n",
        "options = Options()\n",
        "options.add_argument('--headless')\n",
        "options.add_argument('--no-sandbox')\n",
        "options.add_argument('--disable-dev-shm-usage')\n",
        "\n",
        "# استفاده از ChromeDriver\n",
        "service = Service(\"/usr/bin/chromedriver\")\n",
        "driver = webdriver.Chrome(service=service, options=options)\n",
        "\n",
        "# باز کردن صفحه گوگل\n",
        "driver.get(\"https://www.google.com\")\n",
        "\n",
        "# دریافت عنوان صفحه\n",
        "title = driver.title\n",
        "print(f\"عنوان صفحه: {title}\")\n",
        "\n",
        "# بستن مرورگر\n",
        "driver.quit()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mRnfNHdxLo8Z",
        "outputId": "1a6103b8-9374-4779-f139-05874c38e43f"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "عنوان صفحه: Google\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# وارد کردن کتابخانه‌های لازم\n",
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "from selenium.webdriver.common.by import By\n",
        "\n",
        "# تنظیمات Chrome\n",
        "options = Options()\n",
        "options.add_argument(\"--headless\")  # اجرا بدون باز شدن مرورگر\n",
        "options.add_argument(\"--no-sandbox\")\n",
        "options.add_argument(\"--disable-dev-shm-usage\")\n",
        "\n",
        "# راه‌اندازی WebDriver\n",
        "service = Service(\"/usr/bin/chromedriver\")\n",
        "driver = webdriver.Chrome(service=service, options=options)\n",
        "\n",
        "# باز کردن صفحه‌ی SBCها در فوتبین\n",
        "url = \"https://www.futbin.com/squad-building-challenges\"\n",
        "driver.get(url)\n",
        "\n",
        "# گرفتن عنوان صفحه برای تست\n",
        "print(\"عنوان صفحه:\", driver.title)\n",
        "\n",
        "# بستن مرورگر\n",
        "driver.quit()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9DZ1eTMbL9X7",
        "outputId": "ccbfb37c-2b63-489a-f90e-8cb4958c0b2f"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "عنوان صفحه: Just a moment...\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "from selenium.webdriver.common.by import By\n",
        "from selenium.webdriver.support.ui import WebDriverWait\n",
        "from selenium.webdriver.support import expected_conditions as EC\n",
        "\n",
        "# تنظیمات Chrome\n",
        "options = Options()\n",
        "options.add_argument(\"--headless\")  # اجرا بدون باز شدن مرورگر\n",
        "options.add_argument(\"--no-sandbox\")\n",
        "options.add_argument(\"--disable-dev-shm-usage\")\n",
        "\n",
        "# راه‌اندازی WebDriver\n",
        "service = Service(\"/usr/bin/chromedriver\")\n",
        "driver = webdriver.Chrome(service=service, options=options)\n",
        "\n",
        "# باز کردن صفحه‌ی SBCها در فوتبین\n",
        "url = \"https://www.futbin.com/squad-building-challenges\"\n",
        "driver.get(url)\n",
        "\n",
        "# منتظر ماندن برای اینکه صفحه به طور کامل بارگذاری بشه\n",
        "try:\n",
        "    # منتظر ماندن برای اینکه عنصر صفحه بارگذاری بشه\n",
        "    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, \"sbc-item\")))\n",
        "    print(\"صفحه بارگذاری شد!\")\n",
        "\n",
        "    # گرفتن عنوان صفحه برای تست\n",
        "    print(\"عنوان صفحه:\", driver.title)\n",
        "\n",
        "except:\n",
        "    print(\"خطا: صفحه بارگذاری نشد یا زمان تمام شد.\")\n",
        "\n",
        "# بستن مرورگر\n",
        "driver.quit()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2X8wvZ2tMMyo",
        "outputId": "117ee46d-d628-4e33-e600-cdfa04e3cfc3"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "خطا: صفحه بارگذاری نشد یا زمان تمام شد.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from selenium.webdriver.common.by import By\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "from selenium.webdriver.support.ui import WebDriverWait\n",
        "from selenium.webdriver.support import expected_conditions as EC\n",
        "from webdriver_manager.chrome import ChromeDriverManager\n",
        "\n",
        "# تنظیمات مرورگر\n",
        "options = Options()\n",
        "options.add_argument('--headless')  # اجرای مرورگر در حالت بدون نمایش\n",
        "\n",
        "# راه‌اندازی WebDriver\n",
        "service = Service(ChromeDriverManager().install())\n",
        "driver = webdriver.Chrome(service=service, options=options)\n",
        "\n",
        "try:\n",
        "    # وارد شدن به صفحه\n",
        "    driver.get('https://www.futbin.com/squad-building-challenges')\n",
        "\n",
        "    # منتظر می‌مانیم تا صفحه به طور کامل بارگذاری شود\n",
        "    WebDriverWait(driver, 20).until(\n",
        "        EC.presence_of_element_located((By.CLASS_NAME, 'sbc-item'))  # منتظر بارگذاری عنصر خاص (می‌توانید کلاس خود را تغییر دهید)\n",
        "    )\n",
        "\n",
        "    # اگر صفحه به درستی بارگذاری شد، این پیام نمایش داده می‌شود\n",
        "    print(\"صفحه با موفقیت بارگذاری شد!\")\n",
        "\n",
        "    # ادامه کارهای دیگر شما در اینجا...\n",
        "\n",
        "finally:\n",
        "    # بستن مرورگر\n",
        "    driver.quit()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 651
        },
        "id": "n2D-_yRmOgzz",
        "outputId": "92c758cc-d1e2-4796-a8d5-55a4e2877a3a"
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "error",
          "ename": "SessionNotCreatedException",
          "evalue": "Message: session not created: probably user data directory is already in use, please specify a unique value for --user-data-dir argument, or don't use --user-data-dir\nStacktrace:\n#0 0x5afc87be1a1a <unknown>\n#1 0x5afc87699390 <unknown>\n#2 0x5afc876d3109 <unknown>\n#3 0x5afc876ceb5f <unknown>\n#4 0x5afc8771f53f <unknown>\n#5 0x5afc8771ea76 <unknown>\n#6 0x5afc877109a3 <unknown>\n#7 0x5afc876dc60e <unknown>\n#8 0x5afc876dddd1 <unknown>\n#9 0x5afc87ba7ddb <unknown>\n#10 0x5afc87babcbc <unknown>\n#11 0x5afc87b8f392 <unknown>\n#12 0x5afc87bac834 <unknown>\n#13 0x5afc87b731ef <unknown>\n#14 0x5afc87bd0038 <unknown>\n#15 0x5afc87bd0216 <unknown>\n#16 0x5afc87be0896 <unknown>\n#17 0x796ea9c91ac3 <unknown>\n",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mSessionNotCreatedException\u001b[0m                Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-28-1d4b2944115e>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     13\u001b[0m \u001b[0;31m# راه‌اندازی WebDriver\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     14\u001b[0m \u001b[0mservice\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mService\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mChromeDriverManager\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0minstall\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 15\u001b[0;31m \u001b[0mdriver\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     16\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     17\u001b[0m \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chrome/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     43\u001b[0m         \u001b[0moptions\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0mOptions\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     44\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 45\u001b[0;31m         super().__init__(\n\u001b[0m\u001b[1;32m     46\u001b[0m             \u001b[0mbrowser_name\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mDesiredCapabilities\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCHROME\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"browserName\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     47\u001b[0m             \u001b[0mvendor_prefix\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"goog\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chromium/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, browser_name, vendor_prefix, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     64\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     65\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 66\u001b[0;31m             \u001b[0msuper\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__init__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mexecutor\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     67\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     68\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mquit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, command_executor, keep_alive, file_detector, options, locator_converter, web_element_cls, client_config)\u001b[0m\n\u001b[1;32m    248\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_authenticator_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    249\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_client\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 250\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_session\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    251\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_fedcm\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mFedCM\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    252\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mstart_session\u001b[0;34m(self, capabilities)\u001b[0m\n\u001b[1;32m    340\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    341\u001b[0m         \u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_create_caps\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 342\u001b[0;31m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mCommand\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mNEW_SESSION\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcaps\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    343\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msession_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"sessionId\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    344\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"capabilities\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, driver_command, params)\u001b[0m\n\u001b[1;32m    427\u001b[0m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    428\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 429\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    430\u001b[0m             \u001b[0mresponse\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_unwrap_value\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    431\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/errorhandler.py\u001b[0m in \u001b[0;36mcheck_response\u001b[0;34m(self, response)\u001b[0m\n\u001b[1;32m    230\u001b[0m                 \u001b[0malert_text\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"alert\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"text\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    231\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0malert_text\u001b[0m\u001b[0;34m)\u001b[0m  \u001b[0;31m# type: ignore[call-arg]  # mypy is not smart enough here\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 232\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mSessionNotCreatedException\u001b[0m: Message: session not created: probably user data directory is already in use, please specify a unique value for --user-data-dir argument, or don't use --user-data-dir\nStacktrace:\n#0 0x5afc87be1a1a <unknown>\n#1 0x5afc87699390 <unknown>\n#2 0x5afc876d3109 <unknown>\n#3 0x5afc876ceb5f <unknown>\n#4 0x5afc8771f53f <unknown>\n#5 0x5afc8771ea76 <unknown>\n#6 0x5afc877109a3 <unknown>\n#7 0x5afc876dc60e <unknown>\n#8 0x5afc876dddd1 <unknown>\n#9 0x5afc87ba7ddb <unknown>\n#10 0x5afc87babcbc <unknown>\n#11 0x5afc87b8f392 <unknown>\n#12 0x5afc87bac834 <unknown>\n#13 0x5afc87b731ef <unknown>\n#14 0x5afc87bd0038 <unknown>\n#15 0x5afc87bd0216 <unknown>\n#16 0x5afc87be0896 <unknown>\n#17 0x796ea9c91ac3 <unknown>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from selenium.webdriver.common.by import By\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "from selenium.webdriver.support.ui import WebDriverWait\n",
        "from selenium.webdriver.support import expected_conditions as EC\n",
        "from webdriver_manager.chrome import ChromeDriverManager\n",
        "import os\n",
        "\n",
        "# تنظیمات مرورگر\n",
        "options = Options()\n",
        "options.add_argument('--headless')  # اجرای مرورگر در حالت بدون نمایش\n",
        "\n",
        "# اضافه کردن گزینه برای دایرکتوری کاربری منحصر به فرد\n",
        "user_data_dir = \"/tmp/chrome_data\"\n",
        "os.makedirs(user_data_dir, exist_ok=True)\n",
        "options.add_argument(f'--user-data-dir={user_data_dir}')\n",
        "\n",
        "# راه‌اندازی WebDriver\n",
        "service = Service(ChromeDriverManager().install())\n",
        "driver = webdriver.Chrome(service=service, options=options)\n",
        "\n",
        "try:\n",
        "    # وارد شدن به صفحه\n",
        "    driver.get('https://www.futbin.com/squad-building-challenges')\n",
        "\n",
        "    # منتظر می‌مانیم تا صفحه به طور کامل بارگذاری شود\n",
        "    WebDriverWait(driver, 20).until(\n",
        "        EC.presence_of_element_located((By.CLASS_NAME, 'sbc-item'))  # منتظر بارگذاری عنصر خاص\n",
        "    )\n",
        "\n",
        "    # اگر صفحه به درستی بارگذاری شد، این پیام نمایش داده می‌شود\n",
        "    print(\"صفحه با موفقیت بارگذاری شد!\")\n",
        "\n",
        "    # ادامه کارهای دیگر شما در اینجا...\n",
        "\n",
        "finally:\n",
        "    # بستن مرورگر\n",
        "    driver.quit()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 651
        },
        "id": "1aesnJoBOmnT",
        "outputId": "01853b2c-2e1a-4f9e-d095-c1af5b2f44a4"
      },
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "error",
          "ename": "SessionNotCreatedException",
          "evalue": "Message: session not created: probably user data directory is already in use, please specify a unique value for --user-data-dir argument, or don't use --user-data-dir\nStacktrace:\n#0 0x598812f8ea1a <unknown>\n#1 0x598812a46390 <unknown>\n#2 0x598812a80109 <unknown>\n#3 0x598812a7bb5f <unknown>\n#4 0x598812acc53f <unknown>\n#5 0x598812acba76 <unknown>\n#6 0x598812abd9a3 <unknown>\n#7 0x598812a8960e <unknown>\n#8 0x598812a8add1 <unknown>\n#9 0x598812f54ddb <unknown>\n#10 0x598812f58cbc <unknown>\n#11 0x598812f3c392 <unknown>\n#12 0x598812f59834 <unknown>\n#13 0x598812f201ef <unknown>\n#14 0x598812f7d038 <unknown>\n#15 0x598812f7d216 <unknown>\n#16 0x598812f8d896 <unknown>\n#17 0x79802acb9ac3 <unknown>\n",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mSessionNotCreatedException\u001b[0m                Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-29-b20448a8c3a7>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     19\u001b[0m \u001b[0;31m# راه‌اندازی WebDriver\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     20\u001b[0m \u001b[0mservice\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mService\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mChromeDriverManager\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0minstall\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 21\u001b[0;31m \u001b[0mdriver\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     22\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     23\u001b[0m \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chrome/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     43\u001b[0m         \u001b[0moptions\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0mOptions\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     44\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 45\u001b[0;31m         super().__init__(\n\u001b[0m\u001b[1;32m     46\u001b[0m             \u001b[0mbrowser_name\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mDesiredCapabilities\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCHROME\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"browserName\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     47\u001b[0m             \u001b[0mvendor_prefix\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"goog\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chromium/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, browser_name, vendor_prefix, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     64\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     65\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 66\u001b[0;31m             \u001b[0msuper\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__init__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mexecutor\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     67\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     68\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mquit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, command_executor, keep_alive, file_detector, options, locator_converter, web_element_cls, client_config)\u001b[0m\n\u001b[1;32m    248\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_authenticator_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    249\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_client\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 250\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_session\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    251\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_fedcm\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mFedCM\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    252\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mstart_session\u001b[0;34m(self, capabilities)\u001b[0m\n\u001b[1;32m    340\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    341\u001b[0m         \u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_create_caps\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 342\u001b[0;31m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mCommand\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mNEW_SESSION\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcaps\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    343\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msession_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"sessionId\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    344\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"capabilities\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, driver_command, params)\u001b[0m\n\u001b[1;32m    427\u001b[0m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    428\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 429\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    430\u001b[0m             \u001b[0mresponse\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_unwrap_value\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    431\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/errorhandler.py\u001b[0m in \u001b[0;36mcheck_response\u001b[0;34m(self, response)\u001b[0m\n\u001b[1;32m    230\u001b[0m                 \u001b[0malert_text\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"alert\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"text\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    231\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0malert_text\u001b[0m\u001b[0;34m)\u001b[0m  \u001b[0;31m# type: ignore[call-arg]  # mypy is not smart enough here\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 232\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mSessionNotCreatedException\u001b[0m: Message: session not created: probably user data directory is already in use, please specify a unique value for --user-data-dir argument, or don't use --user-data-dir\nStacktrace:\n#0 0x598812f8ea1a <unknown>\n#1 0x598812a46390 <unknown>\n#2 0x598812a80109 <unknown>\n#3 0x598812a7bb5f <unknown>\n#4 0x598812acc53f <unknown>\n#5 0x598812acba76 <unknown>\n#6 0x598812abd9a3 <unknown>\n#7 0x598812a8960e <unknown>\n#8 0x598812a8add1 <unknown>\n#9 0x598812f54ddb <unknown>\n#10 0x598812f58cbc <unknown>\n#11 0x598812f3c392 <unknown>\n#12 0x598812f59834 <unknown>\n#13 0x598812f201ef <unknown>\n#14 0x598812f7d038 <unknown>\n#15 0x598812f7d216 <unknown>\n#16 0x598812f8d896 <unknown>\n#17 0x79802acb9ac3 <unknown>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from selenium.webdriver.common.by import By\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "from selenium.webdriver.support.ui import WebDriverWait\n",
        "from selenium.webdriver.support import expected_conditions as EC\n",
        "from webdriver_manager.chrome import ChromeDriverManager\n",
        "import os\n",
        "import shutil\n",
        "\n",
        "# تنظیمات مرورگر\n",
        "options = Options()\n",
        "options.add_argument('--headless')  # اجرای مرورگر در حالت بدون نمایش\n",
        "\n",
        "# ساخت یک دایرکتوری منحصر به فرد برای داده‌های کاربری\n",
        "user_data_dir = \"/tmp/chrome_data_\" + str(os.getpid())  # استفاده از شناسه فرآیند برای جلوگیری از تداخل\n",
        "os.makedirs(user_data_dir, exist_ok=True)\n",
        "options.add_argument(f'--user-data-dir={user_data_dir}')\n",
        "\n",
        "# راه‌اندازی WebDriver\n",
        "service = Service(ChromeDriverManager().install())\n",
        "driver = webdriver.Chrome(service=service, options=options)\n",
        "\n",
        "try:\n",
        "    # وارد شدن به صفحه\n",
        "    driver.get('https://www.futbin.com/squad-building-challenges')\n",
        "\n",
        "    # منتظر می‌مانیم تا صفحه به طور کامل بارگذاری شود\n",
        "    WebDriverWait(driver, 20).until(\n",
        "        EC.presence_of_element_located((By.CLASS_NAME, 'sbc-item'))  # منتظر بارگذاری عنصر خاص\n",
        "    )\n",
        "\n",
        "    # اگر صفحه به درستی بارگذاری شد، این پیام نمایش داده می‌شود\n",
        "    print(\"صفحه با موفقیت بارگذاری شد!\")\n",
        "\n",
        "    # ادامه کارهای دیگر شما در اینجا...\n",
        "\n",
        "finally:\n",
        "    # بستن مرورگر\n",
        "    driver.quit()\n",
        "\n",
        "    # حذف دایرکتوری داده‌های موقت\n",
        "    shutil.rmtree(user_data_dir)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 651
        },
        "id": "SZ7Nt5klOtch",
        "outputId": "f90ed89a-aec7-4e37-eb29-f3bdc121161d"
      },
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "error",
          "ename": "SessionNotCreatedException",
          "evalue": "Message: session not created: probably user data directory is already in use, please specify a unique value for --user-data-dir argument, or don't use --user-data-dir\nStacktrace:\n#0 0x5557b3ee1a1a <unknown>\n#1 0x5557b3999390 <unknown>\n#2 0x5557b39d3109 <unknown>\n#3 0x5557b39ceb5f <unknown>\n#4 0x5557b3a1f53f <unknown>\n#5 0x5557b3a1ea76 <unknown>\n#6 0x5557b3a109a3 <unknown>\n#7 0x5557b39dc60e <unknown>\n#8 0x5557b39dddd1 <unknown>\n#9 0x5557b3ea7ddb <unknown>\n#10 0x5557b3eabcbc <unknown>\n#11 0x5557b3e8f392 <unknown>\n#12 0x5557b3eac834 <unknown>\n#13 0x5557b3e731ef <unknown>\n#14 0x5557b3ed0038 <unknown>\n#15 0x5557b3ed0216 <unknown>\n#16 0x5557b3ee0896 <unknown>\n#17 0x7a4d8f4faac3 <unknown>\n",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mSessionNotCreatedException\u001b[0m                Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-30-bf5a69683592>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     20\u001b[0m \u001b[0;31m# راه‌اندازی WebDriver\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     21\u001b[0m \u001b[0mservice\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mService\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mChromeDriverManager\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0minstall\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 22\u001b[0;31m \u001b[0mdriver\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     23\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     24\u001b[0m \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chrome/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     43\u001b[0m         \u001b[0moptions\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0mOptions\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     44\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 45\u001b[0;31m         super().__init__(\n\u001b[0m\u001b[1;32m     46\u001b[0m             \u001b[0mbrowser_name\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mDesiredCapabilities\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCHROME\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"browserName\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     47\u001b[0m             \u001b[0mvendor_prefix\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"goog\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chromium/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, browser_name, vendor_prefix, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     64\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     65\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 66\u001b[0;31m             \u001b[0msuper\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__init__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mexecutor\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     67\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     68\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mquit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, command_executor, keep_alive, file_detector, options, locator_converter, web_element_cls, client_config)\u001b[0m\n\u001b[1;32m    248\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_authenticator_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    249\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_client\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 250\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_session\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    251\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_fedcm\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mFedCM\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    252\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mstart_session\u001b[0;34m(self, capabilities)\u001b[0m\n\u001b[1;32m    340\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    341\u001b[0m         \u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_create_caps\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 342\u001b[0;31m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mCommand\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mNEW_SESSION\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcaps\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    343\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msession_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"sessionId\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    344\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"capabilities\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, driver_command, params)\u001b[0m\n\u001b[1;32m    427\u001b[0m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    428\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 429\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    430\u001b[0m             \u001b[0mresponse\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_unwrap_value\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    431\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/errorhandler.py\u001b[0m in \u001b[0;36mcheck_response\u001b[0;34m(self, response)\u001b[0m\n\u001b[1;32m    230\u001b[0m                 \u001b[0malert_text\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"alert\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"text\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    231\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0malert_text\u001b[0m\u001b[0;34m)\u001b[0m  \u001b[0;31m# type: ignore[call-arg]  # mypy is not smart enough here\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 232\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mSessionNotCreatedException\u001b[0m: Message: session not created: probably user data directory is already in use, please specify a unique value for --user-data-dir argument, or don't use --user-data-dir\nStacktrace:\n#0 0x5557b3ee1a1a <unknown>\n#1 0x5557b3999390 <unknown>\n#2 0x5557b39d3109 <unknown>\n#3 0x5557b39ceb5f <unknown>\n#4 0x5557b3a1f53f <unknown>\n#5 0x5557b3a1ea76 <unknown>\n#6 0x5557b3a109a3 <unknown>\n#7 0x5557b39dc60e <unknown>\n#8 0x5557b39dddd1 <unknown>\n#9 0x5557b3ea7ddb <unknown>\n#10 0x5557b3eabcbc <unknown>\n#11 0x5557b3e8f392 <unknown>\n#12 0x5557b3eac834 <unknown>\n#13 0x5557b3e731ef <unknown>\n#14 0x5557b3ed0038 <unknown>\n#15 0x5557b3ed0216 <unknown>\n#16 0x5557b3ee0896 <unknown>\n#17 0x7a4d8f4faac3 <unknown>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "from webdriver_manager.chrome import ChromeDriverManager\n",
        "import os\n",
        "import shutil\n",
        "\n",
        "# تنظیمات مرورگر\n",
        "options = Options()\n",
        "options.add_argument('--headless')  # اجرای مرورگر در حالت بدون نمایش\n",
        "options.add_argument('--no-sandbox')  # برای جلوگیری از ارور در بعضی از محیط‌ها\n",
        "\n",
        "# ساخت یک دایرکتوری منحصر به فرد برای داده‌های کاربری\n",
        "user_data_dir = \"/tmp/chrome_data_\" + str(os.getpid())  # استفاده از شناسه فرآیند برای جلوگیری از تداخل\n",
        "os.makedirs(user_data_dir, exist_ok=True)\n",
        "options.add_argument(f'--user-data-dir={user_data_dir}')\n",
        "\n",
        "# راه‌اندازی WebDriver\n",
        "service = Service(ChromeDriverManager().install())\n",
        "driver = webdriver.Chrome(service=service, options=options)\n",
        "\n",
        "try:\n",
        "    # وارد شدن به صفحه\n",
        "    driver.get('https://www.futbin.com/squad-building-challenges')\n",
        "\n",
        "    # منتظر می‌مانیم تا صفحه به طور کامل بارگذاری شود\n",
        "    WebDriverWait(driver,\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 106
        },
        "id": "aupGicN8O6rz",
        "outputId": "f3b22c2d-7853-4659-eb04-69997d40c55a"
      },
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "error",
          "ename": "SyntaxError",
          "evalue": "incomplete input (<ipython-input-31-a1fb5e52f44c>, line 27)",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-31-a1fb5e52f44c>\"\u001b[0;36m, line \u001b[0;32m27\u001b[0m\n\u001b[0;31m    WebDriverWait(driver,\u001b[0m\n\u001b[0m                          ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m incomplete input\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "from webdriver_manager.chrome import ChromeDriverManager\n",
        "from selenium.webdriver.common.by import By\n",
        "from selenium.webdriver.support.ui import WebDriverWait\n",
        "from selenium.webdriver.support import expected_conditions as EC\n",
        "import os\n",
        "import shutil\n",
        "\n",
        "# تنظیمات مرورگر\n",
        "options = Options()\n",
        "options.add_argument('--headless')  # اجرای مرورگر در حالت بدون نمایش\n",
        "options.add_argument('--no-sandbox')  # برای جلوگیری از ارور در بعضی از محیط‌ها\n",
        "\n",
        "# ساخت یک دایرکتوری منحصر به فرد برای داده‌های کاربری\n",
        "user_data_dir = \"/tmp/chrome_data_\" + str(os.getpid())  # استفاده از شناسه فرآیند برای جلوگیری از تداخل\n",
        "os.makedirs(user_data_dir, exist_ok=True)\n",
        "options.add_argument(f'--user-data-dir={user_data_dir}')\n",
        "\n",
        "# راه‌اندازی WebDriver\n",
        "service = Service(ChromeDriverManager().install())\n",
        "driver = webdriver.Chrome(service=service, options=options)\n",
        "\n",
        "try:\n",
        "    # وارد شدن به صفحه\n",
        "    driver.get('https://www.futbin.com/squad-building-challenges')\n",
        "\n",
        "    # منتظر می‌مانیم تا صفحه به طور کامل بارگذاری شود\n",
        "    WebDriverWait(driver, 20).until(\n",
        "        EC.presence_of_element_located((By.CLASS_NAME, 'sbc-item'))  # منتظر بارگذاری عنصر خاص\n",
        "    )\n",
        "\n",
        "    # اگر صفحه به درستی بارگذاری شد، این پیام نمایش داده می‌شود\n",
        "    print(\"صفحه با موفقیت بارگذاری شد!\")\n",
        "\n",
        "finally:\n",
        "    # بستن مرورگر\n",
        "    driver.quit()\n",
        "\n",
        "    # حذف دایرکتوری داده‌های موقت\n",
        "    shutil.rmtree(user_data_dir)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 679
        },
        "id": "2NoD8pyFPBMh",
        "outputId": "35450ac5-5dc4-4551-8498-8e1f4d3d1bdb"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "error",
          "ename": "TimeoutException",
          "evalue": "Message: \nStacktrace:\n#0 0x5cc3fda02a1a <unknown>\n#1 0x5cc3fd4ba390 <unknown>\n#2 0x5cc3fd50bc85 <unknown>\n#3 0x5cc3fd50beb1 <unknown>\n#4 0x5cc3fd55ad64 <unknown>\n#5 0x5cc3fd531bfd <unknown>\n#6 0x5cc3fd55807b <unknown>\n#7 0x5cc3fd5319a3 <unknown>\n#8 0x5cc3fd4fd60e <unknown>\n#9 0x5cc3fd4fedd1 <unknown>\n#10 0x5cc3fd9c8ddb <unknown>\n#11 0x5cc3fd9cccbc <unknown>\n#12 0x5cc3fd9b0392 <unknown>\n#13 0x5cc3fd9cd834 <unknown>\n#14 0x5cc3fd9941ef <unknown>\n#15 0x5cc3fd9f1038 <unknown>\n#16 0x5cc3fd9f1216 <unknown>\n#17 0x5cc3fda01896 <unknown>\n#18 0x7c74a73e4ac3 <unknown>\n",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTimeoutException\u001b[0m                          Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-32-cbea7fb8a568>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     28\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     29\u001b[0m     \u001b[0;31m# منتظر می‌مانیم تا صفحه به طور کامل بارگذاری شود\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 30\u001b[0;31m     WebDriverWait(driver, 20).until(\n\u001b[0m\u001b[1;32m     31\u001b[0m         \u001b[0mEC\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpresence_of_element_located\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mBy\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCLASS_NAME\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'sbc-item'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m  \u001b[0;31m# منتظر بارگذاری عنصر خاص\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     32\u001b[0m     )\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/support/wait.py\u001b[0m in \u001b[0;36muntil\u001b[0;34m(self, method, message)\u001b[0m\n\u001b[1;32m    144\u001b[0m                 \u001b[0;32mbreak\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    145\u001b[0m             \u001b[0mtime\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msleep\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_poll\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 146\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mTimeoutException\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    147\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    148\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0muntil_not\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmethod\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mCallable\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mD\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mT\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmessage\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mstr\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m\"\"\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m->\u001b[0m \u001b[0mUnion\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mT\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mLiteral\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mTimeoutException\u001b[0m: Message: \nStacktrace:\n#0 0x5cc3fda02a1a <unknown>\n#1 0x5cc3fd4ba390 <unknown>\n#2 0x5cc3fd50bc85 <unknown>\n#3 0x5cc3fd50beb1 <unknown>\n#4 0x5cc3fd55ad64 <unknown>\n#5 0x5cc3fd531bfd <unknown>\n#6 0x5cc3fd55807b <unknown>\n#7 0x5cc3fd5319a3 <unknown>\n#8 0x5cc3fd4fd60e <unknown>\n#9 0x5cc3fd4fedd1 <unknown>\n#10 0x5cc3fd9c8ddb <unknown>\n#11 0x5cc3fd9cccbc <unknown>\n#12 0x5cc3fd9b0392 <unknown>\n#13 0x5cc3fd9cd834 <unknown>\n#14 0x5cc3fd9941ef <unknown>\n#15 0x5cc3fd9f1038 <unknown>\n#16 0x5cc3fd9f1216 <unknown>\n#17 0x5cc3fda01896 <unknown>\n#18 0x7c74a73e4ac3 <unknown>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "from webdriver_manager.chrome import ChromeDriverManager\n",
        "from selenium.webdriver.common.by import By\n",
        "from selenium.webdriver.support.ui import WebDriverWait\n",
        "from selenium.webdriver.support import expected_conditions as EC\n",
        "import os\n",
        "import shutil\n",
        "\n",
        "# تنظیمات مرورگر\n",
        "options = Options()\n",
        "options.add_argument('--headless')  # اجرای مرورگر در حالت بدون نمایش\n",
        "options.add_argument('--no-sandbox')  # برای جلوگیری از ارور در بعضی از محیط‌ها\n",
        "\n",
        "# ساخت یک دایرکتوری منحصر به فرد برای داده‌های کاربری\n",
        "user_data_dir = \"/tmp/chrome_data_\" + str(os.getpid())  # استفاده از شناسه فرآیند برای جلوگیری از تداخل\n",
        "os.makedirs(user_data_dir, exist_ok=True)\n",
        "options.add_argument(f'--user-data-dir={user_data_dir}')\n",
        "\n",
        "# راه‌اندازی WebDriver\n",
        "service = Service(ChromeDriverManager().install())\n",
        "driver = webdriver.Chrome(service=service, options=options)\n",
        "\n",
        "try:\n",
        "    # وارد شدن به صفحه\n",
        "    driver.get('https://www.futbin.com/squad-building-challenges')\n",
        "\n",
        "    # منتظر می‌مانیم تا صفحه به طور کامل بارگذاری شود\n",
        "    WebDriverWait(driver, 30).until(\n",
        "        EC.visibility_of_element_located((By.CLASS_NAME, 'sbc-item'))  # منتظر بارگذاری عنصر خاص\n",
        "    )\n",
        "\n",
        "    # اگر صفحه به درستی بارگذاری شد، این پیام نمایش داده می‌شود\n",
        "    print(\"صفحه با موفقیت بارگذاری شد!\")\n",
        "\n",
        "finally:\n",
        "    # بستن مرورگر\n",
        "    driver.quit()\n",
        "\n",
        "    # حذف دایرکتوری داده‌های موقت\n",
        "    shutil.rmtree(user_data_dir)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 679
        },
        "id": "kumHwJ4gPOAP",
        "outputId": "45638740-7703-4275-915b-fe8a2289fbfb"
      },
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "error",
          "ename": "TimeoutException",
          "evalue": "Message: \nStacktrace:\n#0 0x5af440679a1a <unknown>\n#1 0x5af440131390 <unknown>\n#2 0x5af440182c85 <unknown>\n#3 0x5af440182eb1 <unknown>\n#4 0x5af4401d1d64 <unknown>\n#5 0x5af4401a8bfd <unknown>\n#6 0x5af4401cf07b <unknown>\n#7 0x5af4401a89a3 <unknown>\n#8 0x5af44017460e <unknown>\n#9 0x5af440175dd1 <unknown>\n#10 0x5af44063fddb <unknown>\n#11 0x5af440643cbc <unknown>\n#12 0x5af440627392 <unknown>\n#13 0x5af440644834 <unknown>\n#14 0x5af44060b1ef <unknown>\n#15 0x5af440668038 <unknown>\n#16 0x5af440668216 <unknown>\n#17 0x5af440678896 <unknown>\n#18 0x7bd6b9967ac3 <unknown>\n",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTimeoutException\u001b[0m                          Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-33-7e9df55c6eb9>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     28\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     29\u001b[0m     \u001b[0;31m# منتظر می‌مانیم تا صفحه به طور کامل بارگذاری شود\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 30\u001b[0;31m     WebDriverWait(driver, 30).until(\n\u001b[0m\u001b[1;32m     31\u001b[0m         \u001b[0mEC\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mvisibility_of_element_located\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mBy\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCLASS_NAME\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'sbc-item'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m  \u001b[0;31m# منتظر بارگذاری عنصر خاص\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     32\u001b[0m     )\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/support/wait.py\u001b[0m in \u001b[0;36muntil\u001b[0;34m(self, method, message)\u001b[0m\n\u001b[1;32m    144\u001b[0m                 \u001b[0;32mbreak\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    145\u001b[0m             \u001b[0mtime\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msleep\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_poll\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 146\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mTimeoutException\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    147\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    148\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0muntil_not\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmethod\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mCallable\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mD\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mT\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmessage\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mstr\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m\"\"\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m->\u001b[0m \u001b[0mUnion\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mT\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mLiteral\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mTimeoutException\u001b[0m: Message: \nStacktrace:\n#0 0x5af440679a1a <unknown>\n#1 0x5af440131390 <unknown>\n#2 0x5af440182c85 <unknown>\n#3 0x5af440182eb1 <unknown>\n#4 0x5af4401d1d64 <unknown>\n#5 0x5af4401a8bfd <unknown>\n#6 0x5af4401cf07b <unknown>\n#7 0x5af4401a89a3 <unknown>\n#8 0x5af44017460e <unknown>\n#9 0x5af440175dd1 <unknown>\n#10 0x5af44063fddb <unknown>\n#11 0x5af440643cbc <unknown>\n#12 0x5af440627392 <unknown>\n#13 0x5af440644834 <unknown>\n#14 0x5af44060b1ef <unknown>\n#15 0x5af440668038 <unknown>\n#16 0x5af440668216 <unknown>\n#17 0x5af440678896 <unknown>\n#18 0x7bd6b9967ac3 <unknown>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from selenium.webdriver.common.by import By\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "from webdriver_manager.chrome import ChromeDriverManager\n",
        "from selenium.webdriver.support.ui import WebDriverWait\n",
        "from selenium.webdriver.support import expected_conditions as EC\n",
        "\n",
        "# تنظیمات Chrome برای استفاده بدون نمایش GUI (headless)\n",
        "options = Options()\n",
        "options.add_argument('--headless')  # استفاده از حالت بدون صفحه\n",
        "options.add_argument('--no-sandbox')\n",
        "options.add_argument('--disable-dev-shm-usage')\n",
        "\n",
        "# راه‌اندازی WebDriver\n",
        "service = Service(ChromeDriverManager().install())\n",
        "driver = webdriver.Chrome(service=service, options=options)\n",
        "\n",
        "try:\n",
        "    # باز کردن صفحه\n",
        "    driver.get('https://www.futbin.com/')  # آدرس سایت را اینجا وارد کنید\n",
        "\n",
        "    # منتظر می‌مانیم تا عنصر مربوطه به صفحه اضافه شود\n",
        "    WebDriverWait(driver, 30).until(\n",
        "        EC.presence_of_element_located((By.XPATH, '//*[contains(text(), \"squad building challenges\")]'))\n",
        "    )\n",
        "\n",
        "    # ادامه مراحل بعدی که نیاز دارید (مثل استخراج داده یا تعامل با عناصر صفحه)\n",
        "    print(\"عنصر پیدا شد و صفحه بارگذاری شد.\")\n",
        "\n",
        "finally:\n",
        "    # بستن مرورگر\n",
        "    driver.quit()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 679
        },
        "id": "7zehi3VeRm8F",
        "outputId": "22d4603b-b611-4d2e-913d-b3f0dac0f406"
      },
      "execution_count": 34,
      "outputs": [
        {
          "output_type": "error",
          "ename": "TimeoutException",
          "evalue": "Message: \nStacktrace:\n#0 0x5985df0c7a1a <unknown>\n#1 0x5985deb7f390 <unknown>\n#2 0x5985debd0c85 <unknown>\n#3 0x5985debd0eb1 <unknown>\n#4 0x5985dec1fd64 <unknown>\n#5 0x5985debf6bfd <unknown>\n#6 0x5985dec1d07b <unknown>\n#7 0x5985debf69a3 <unknown>\n#8 0x5985debc260e <unknown>\n#9 0x5985debc3dd1 <unknown>\n#10 0x5985df08dddb <unknown>\n#11 0x5985df091cbc <unknown>\n#12 0x5985df075392 <unknown>\n#13 0x5985df092834 <unknown>\n#14 0x5985df0591ef <unknown>\n#15 0x5985df0b6038 <unknown>\n#16 0x5985df0b6216 <unknown>\n#17 0x5985df0c6896 <unknown>\n#18 0x7b1feec6fac3 <unknown>\n",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTimeoutException\u001b[0m                          Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-34-3cf7ee5b5080>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     22\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     23\u001b[0m     \u001b[0;31m# منتظر می‌مانیم تا عنصر مربوطه به صفحه اضافه شود\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 24\u001b[0;31m     WebDriverWait(driver, 30).until(\n\u001b[0m\u001b[1;32m     25\u001b[0m         \u001b[0mEC\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpresence_of_element_located\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mBy\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mXPATH\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'//*[contains(text(), \"squad building challenges\")]'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     26\u001b[0m     )\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/support/wait.py\u001b[0m in \u001b[0;36muntil\u001b[0;34m(self, method, message)\u001b[0m\n\u001b[1;32m    144\u001b[0m                 \u001b[0;32mbreak\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    145\u001b[0m             \u001b[0mtime\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msleep\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_poll\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 146\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mTimeoutException\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    147\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    148\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0muntil_not\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmethod\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mCallable\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mD\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mT\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmessage\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mstr\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m\"\"\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m->\u001b[0m \u001b[0mUnion\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mT\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mLiteral\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mTimeoutException\u001b[0m: Message: \nStacktrace:\n#0 0x5985df0c7a1a <unknown>\n#1 0x5985deb7f390 <unknown>\n#2 0x5985debd0c85 <unknown>\n#3 0x5985debd0eb1 <unknown>\n#4 0x5985dec1fd64 <unknown>\n#5 0x5985debf6bfd <unknown>\n#6 0x5985dec1d07b <unknown>\n#7 0x5985debf69a3 <unknown>\n#8 0x5985debc260e <unknown>\n#9 0x5985debc3dd1 <unknown>\n#10 0x5985df08dddb <unknown>\n#11 0x5985df091cbc <unknown>\n#12 0x5985df075392 <unknown>\n#13 0x5985df092834 <unknown>\n#14 0x5985df0591ef <unknown>\n#15 0x5985df0b6038 <unknown>\n#16 0x5985df0b6216 <unknown>\n#17 0x5985df0c6896 <unknown>\n#18 0x7b1feec6fac3 <unknown>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from selenium.webdriver.common.by import By\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "from webdriver_manager.chrome import ChromeDriverManager\n",
        "from selenium.webdriver.support.ui import WebDriverWait\n",
        "from selenium.webdriver.support import expected_conditions as EC\n",
        "\n",
        "# تنظیمات Chrome برای استفاده بدون نمایش GUI (headless)\n",
        "options = Options()\n",
        "options.add_argument('--headless')  # استفاده از حالت بدون صفحه\n",
        "options.add_argument('--no-sandbox')\n",
        "options.add_argument('--disable-dev-shm-usage')\n",
        "\n",
        "# راه‌اندازی WebDriver\n",
        "service = Service(ChromeDriverManager().install())\n",
        "driver = webdriver.Chrome(service=service, options=options)\n",
        "\n",
        "try:\n",
        "    # باز کردن صفحه\n",
        "    driver.get('https://www.futbin.com/')  # آدرس سایت را اینجا وارد کنید\n",
        "\n",
        "    # منتظر می‌مانیم تا عنصر مربوطه به صفحه اضافه شود\n",
        "    WebDriverWait(driver, 30).until(\n",
        "        EC.presence_of_element_located((By.CLASS_NAME, 'sbcc-card'))  # به جای \"sbc-item\"، از \"sbcc-card\" استفاده کنید\n",
        "    )\n",
        "\n",
        "    # ادامه مراحل بعدی که نیاز دارید (مثل استخراج داده یا تعامل با عناصر صفحه)\n",
        "    print(\"عنصر پیدا شد و صفحه بارگذاری شد.\")\n",
        "\n",
        "finally:\n",
        "    # بستن مرورگر\n",
        "    driver.quit()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 679
        },
        "id": "E6FQklg7SGNF",
        "outputId": "e59864a7-64f1-4c1f-8cc0-15bb1e48bf51"
      },
      "execution_count": 35,
      "outputs": [
        {
          "ename": "TimeoutException",
          "evalue": "Message: \nStacktrace:\n#0 0x59be63a6fa1a <unknown>\n#1 0x59be63527390 <unknown>\n#2 0x59be63578c85 <unknown>\n#3 0x59be63578eb1 <unknown>\n#4 0x59be635c7d64 <unknown>\n#5 0x59be6359ebfd <unknown>\n#6 0x59be635c507b <unknown>\n#7 0x59be6359e9a3 <unknown>\n#8 0x59be6356a60e <unknown>\n#9 0x59be6356bdd1 <unknown>\n#10 0x59be63a35ddb <unknown>\n#11 0x59be63a39cbc <unknown>\n#12 0x59be63a1d392 <unknown>\n#13 0x59be63a3a834 <unknown>\n#14 0x59be63a011ef <unknown>\n#15 0x59be63a5e038 <unknown>\n#16 0x59be63a5e216 <unknown>\n#17 0x59be63a6e896 <unknown>\n#18 0x7f723c048ac3 <unknown>\n",
          "output_type": "error",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTimeoutException\u001b[0m                          Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-35-0a3fe7edb964>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     22\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     23\u001b[0m     \u001b[0;31m# منتظر می‌مانیم تا عنصر مربوطه به صفحه اضافه شود\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 24\u001b[0;31m     WebDriverWait(driver, 30).until(\n\u001b[0m\u001b[1;32m     25\u001b[0m         \u001b[0mEC\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpresence_of_element_located\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mBy\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCLASS_NAME\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'sbcc-card'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m  \u001b[0;31m# به جای \"sbc-item\"، از \"sbcc-card\" استفاده کنید\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     26\u001b[0m     )\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/support/wait.py\u001b[0m in \u001b[0;36muntil\u001b[0;34m(self, method, message)\u001b[0m\n\u001b[1;32m    144\u001b[0m                 \u001b[0;32mbreak\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    145\u001b[0m             \u001b[0mtime\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msleep\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_poll\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 146\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mTimeoutException\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    147\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    148\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0muntil_not\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmethod\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mCallable\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mD\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mT\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmessage\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mstr\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m\"\"\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m->\u001b[0m \u001b[0mUnion\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mT\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mLiteral\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mTimeoutException\u001b[0m: Message: \nStacktrace:\n#0 0x59be63a6fa1a <unknown>\n#1 0x59be63527390 <unknown>\n#2 0x59be63578c85 <unknown>\n#3 0x59be63578eb1 <unknown>\n#4 0x59be635c7d64 <unknown>\n#5 0x59be6359ebfd <unknown>\n#6 0x59be635c507b <unknown>\n#7 0x59be6359e9a3 <unknown>\n#8 0x59be6356a60e <unknown>\n#9 0x59be6356bdd1 <unknown>\n#10 0x59be63a35ddb <unknown>\n#11 0x59be63a39cbc <unknown>\n#12 0x59be63a1d392 <unknown>\n#13 0x59be63a3a834 <unknown>\n#14 0x59be63a011ef <unknown>\n#15 0x59be63a5e038 <unknown>\n#16 0x59be63a5e216 <unknown>\n#17 0x59be63a6e896 <unknown>\n#18 0x7f723c048ac3 <unknown>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "element = WebDriverWait(driver, 30).until(\n",
        "    EC.presence_of_element_located((By.XPATH, '//a[@href=\"/squad-building-challenges\"]'))\n",
        ")\n",
        "element.click()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 193
        },
        "id": "GPpJGN9Eavhx",
        "outputId": "a3e7fbb6-7bbb-4c74-8b6f-262fcf3f06d4"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "name 'WebDriverWait' is not defined",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-1-2cecde2f962b>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m element = WebDriverWait(driver, 30).until(\n\u001b[0m\u001b[1;32m      2\u001b[0m     \u001b[0mEC\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpresence_of_element_located\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mBy\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mXPATH\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'//a[@href=\"/squad-building-challenges\"]'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m )\n\u001b[1;32m      4\u001b[0m \u001b[0melement\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mclick\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mNameError\u001b[0m: name 'WebDriverWait' is not defined"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from selenium.webdriver.common.by import By\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "from webdriver_manager.chrome import ChromeDriverManager\n",
        "from selenium.webdriver.support.ui import WebDriverWait\n",
        "from selenium.webdriver.support import expected_conditions as EC\n",
        "\n",
        "# تنظیمات Chrome برای اجرای بدون رابط گرافیکی (Headless)\n",
        "options = Options()\n",
        "options.add_argument('--headless')\n",
        "options.add_argument('--no-sandbox')\n",
        "options.add_argument('--disable-dev-shm-usage')\n",
        "\n",
        "# راه‌اندازی WebDriver\n",
        "service = Service(ChromeDriverManager().install())\n",
        "driver = webdriver.Chrome(service=service, options=options)\n",
        "\n",
        "try:\n",
        "    # باز کردن سایت Futbin\n",
        "    driver.get('https://www.futbin.com/')\n",
        "\n",
        "    # منتظر شدن تا لینک \"SBCs\" در منو بارگذاری شود\n",
        "    sbc_link = WebDriverWait(driver, 30).until(\n",
        "        EC.presence_of_element_located((By.XPATH, '//a[@href=\"/squad-building-challenges\"]'))\n",
        "    )\n",
        "\n",
        "    # کلیک روی لینک SBCs\n",
        "    sbc_link.click()\n",
        "\n",
        "    # منتظر شدن تا صفحه SBCs بارگذاری شود\n",
        "    WebDriverWait(driver, 30).until(\n",
        "        EC.presence_of_element_located((By.CLASS_NAME, 'sbcc-card'))  # این کلاس را بررسی کن که درست باشد\n",
        "    )\n",
        "\n",
        "    print(\"صفحه SBCs با موفقیت بارگذاری شد.\")\n",
        "\n",
        "finally:\n",
        "    # بستن مرورگر\n",
        "    driver.quit()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 383
        },
        "id": "xDPb-f9ta9dV",
        "outputId": "86a73bb6-dd3e-40a9-a7d8-7252485f665d"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "error",
          "ename": "ModuleNotFoundError",
          "evalue": "No module named 'selenium'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-2-4a593b22370e>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mselenium\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mselenium\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mchrome\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mservice\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mService\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mselenium\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommon\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mby\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mBy\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mselenium\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mchrome\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0moptions\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mOptions\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mwebdriver_manager\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mchrome\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mChromeDriverManager\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'selenium'",
            "",
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0;32m\nNOTE: If your import is failing due to a missing package, you can\nmanually install dependencies using either !pip or !apt.\n\nTo view examples of installing some common dependencies, click the\n\"Open Examples\" button below.\n\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n"
          ],
          "errorDetails": {
            "actions": [
              {
                "action": "open_url",
                "actionText": "Open Examples",
                "url": "/notebooks/snippets/importing_libraries.ipynb"
              }
            ]
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install selenium\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vLWz9QX9bGkT",
        "outputId": "c0e5a090-298e-4aa7-ac7a-8a185fc10209"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting selenium\n",
            "  Downloading selenium-4.29.0-py3-none-any.whl.metadata (7.1 kB)\n",
            "Requirement already satisfied: urllib3<3,>=1.26 in /usr/local/lib/python3.11/dist-packages (from urllib3[socks]<3,>=1.26->selenium) (2.3.0)\n",
            "Collecting trio~=0.17 (from selenium)\n",
            "  Downloading trio-0.29.0-py3-none-any.whl.metadata (8.5 kB)\n",
            "Collecting trio-websocket~=0.9 (from selenium)\n",
            "  Downloading trio_websocket-0.12.2-py3-none-any.whl.metadata (5.1 kB)\n",
            "Requirement already satisfied: certifi>=2021.10.8 in /usr/local/lib/python3.11/dist-packages (from selenium) (2025.1.31)\n",
            "Requirement already satisfied: typing_extensions~=4.9 in /usr/local/lib/python3.11/dist-packages (from selenium) (4.12.2)\n",
            "Requirement already satisfied: websocket-client~=1.8 in /usr/local/lib/python3.11/dist-packages (from selenium) (1.8.0)\n",
            "Requirement already satisfied: attrs>=23.2.0 in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (25.1.0)\n",
            "Requirement already satisfied: sortedcontainers in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (2.4.0)\n",
            "Requirement already satisfied: idna in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (3.10)\n",
            "Collecting outcome (from trio~=0.17->selenium)\n",
            "  Downloading outcome-1.3.0.post0-py2.py3-none-any.whl.metadata (2.6 kB)\n",
            "Requirement already satisfied: sniffio>=1.3.0 in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (1.3.1)\n",
            "Collecting wsproto>=0.14 (from trio-websocket~=0.9->selenium)\n",
            "  Downloading wsproto-1.2.0-py3-none-any.whl.metadata (5.6 kB)\n",
            "Requirement already satisfied: pysocks!=1.5.7,<2.0,>=1.5.6 in /usr/local/lib/python3.11/dist-packages (from urllib3[socks]<3,>=1.26->selenium) (1.7.1)\n",
            "Requirement already satisfied: h11<1,>=0.9.0 in /usr/local/lib/python3.11/dist-packages (from wsproto>=0.14->trio-websocket~=0.9->selenium) (0.14.0)\n",
            "Downloading selenium-4.29.0-py3-none-any.whl (9.5 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m9.5/9.5 MB\u001b[0m \u001b[31m51.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading trio-0.29.0-py3-none-any.whl (492 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m492.9/492.9 kB\u001b[0m \u001b[31m27.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading trio_websocket-0.12.2-py3-none-any.whl (21 kB)\n",
            "Downloading outcome-1.3.0.post0-py2.py3-none-any.whl (10 kB)\n",
            "Downloading wsproto-1.2.0-py3-none-any.whl (24 kB)\n",
            "Installing collected packages: wsproto, outcome, trio, trio-websocket, selenium\n",
            "Successfully installed outcome-1.3.0.post0 selenium-4.29.0 trio-0.29.0 trio-websocket-0.12.2 wsproto-1.2.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from selenium.webdriver.common.by import By\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "from webdriver_manager.chrome import ChromeDriverManager\n",
        "from selenium.webdriver.support.ui import WebDriverWait\n",
        "from selenium.webdriver.support import expected_conditions as EC\n",
        "\n",
        "# تنظیمات Chrome برای اجرای بدون رابط گرافیکی (Headless)\n",
        "options = Options()\n",
        "options.add_argument('--headless')\n",
        "options.add_argument('--no-sandbox')\n",
        "options.add_argument('--disable-dev-shm-usage')\n",
        "\n",
        "# راه‌اندازی WebDriver\n",
        "service = Service(ChromeDriverManager().install())\n",
        "driver = webdriver.Chrome(service=service, options=options)\n",
        "\n",
        "try:\n",
        "    # باز کردن سایت Futbin\n",
        "    driver.get('https://www.futbin.com/')\n",
        "\n",
        "    # منتظر شدن تا لینک \"SBCs\" در منو بارگذاری شود\n",
        "    sbc_link = WebDriverWait(driver, 30).until(\n",
        "        EC.presence_of_element_located((By.XPATH, '//a[@href=\"/squad-building-challenges\"]'))\n",
        "    )\n",
        "\n",
        "    # کلیک روی لینک SBCs\n",
        "    sbc_link.click()\n",
        "\n",
        "    # منتظر شدن تا صفحه SBCs بارگذاری شود\n",
        "    WebDriverWait(driver, 30).until(\n",
        "        EC.presence_of_element_located((By.CLASS_NAME, 'sbcc-card'))  # این کلاس را بررسی کن که درست باشد\n",
        "    )\n",
        "\n",
        "    print(\"صفحه SBCs با موفقیت بارگذاری شد.\")\n",
        "\n",
        "finally:\n",
        "    # بستن مرورگر\n",
        "    driver.quit()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 383
        },
        "id": "7suT390zbJpK",
        "outputId": "1aad1bf3-b730-4493-c8e7-33495a0de8f3"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "error",
          "ename": "ModuleNotFoundError",
          "evalue": "No module named 'webdriver_manager'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-4-4a593b22370e>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mselenium\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommon\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mby\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mBy\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mselenium\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mchrome\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0moptions\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mOptions\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 5\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mwebdriver_manager\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mchrome\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mChromeDriverManager\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      6\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mselenium\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msupport\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mui\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mWebDriverWait\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      7\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mselenium\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msupport\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mexpected_conditions\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mEC\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'webdriver_manager'",
            "",
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0;32m\nNOTE: If your import is failing due to a missing package, you can\nmanually install dependencies using either !pip or !apt.\n\nTo view examples of installing some common dependencies, click the\n\"Open Examples\" button below.\n\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n"
          ],
          "errorDetails": {
            "actions": [
              {
                "action": "open_url",
                "actionText": "Open Examples",
                "url": "/notebooks/snippets/importing_libraries.ipynb"
              }
            ]
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install webdriver-manager\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8INse8p6bQ9i",
        "outputId": "3d0e1a8b-4fbd-4dce-f855-95d610f56108"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting webdriver-manager\n",
            "  Downloading webdriver_manager-4.0.2-py2.py3-none-any.whl.metadata (12 kB)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.11/dist-packages (from webdriver-manager) (2.32.3)\n",
            "Collecting python-dotenv (from webdriver-manager)\n",
            "  Downloading python_dotenv-1.0.1-py3-none-any.whl.metadata (23 kB)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.11/dist-packages (from webdriver-manager) (24.2)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests->webdriver-manager) (3.4.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests->webdriver-manager) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests->webdriver-manager) (2.3.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests->webdriver-manager) (2025.1.31)\n",
            "Downloading webdriver_manager-4.0.2-py2.py3-none-any.whl (27 kB)\n",
            "Downloading python_dotenv-1.0.1-py3-none-any.whl (19 kB)\n",
            "Installing collected packages: python-dotenv, webdriver-manager\n",
            "Successfully installed python-dotenv-1.0.1 webdriver-manager-4.0.2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from selenium.webdriver.common.by import By\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "from webdriver_manager.chrome import ChromeDriverManager\n",
        "from selenium.webdriver.support.ui import WebDriverWait\n",
        "from selenium.webdriver.support import expected_conditions as EC\n",
        "\n",
        "# تنظیمات Chrome برای اجرای بدون رابط گرافیکی (Headless)\n",
        "options = Options()\n",
        "options.add_argument('--headless')\n",
        "options.add_argument('--no-sandbox')\n",
        "options.add_argument('--disable-dev-shm-usage')\n",
        "\n",
        "# راه‌اندازی WebDriver\n",
        "service = Service(ChromeDriverManager().install())\n",
        "driver = webdriver.Chrome(service=service, options=options)\n",
        "\n",
        "try:\n",
        "    # باز کردن سایت Futbin\n",
        "    driver.get('https://www.futbin.com/')\n",
        "\n",
        "    # منتظر شدن تا لینک \"SBCs\" در منو بارگذاری شود\n",
        "    sbc_link = WebDriverWait(driver, 30).until(\n",
        "        EC.presence_of_element_located((By.XPATH, '//a[@href=\"/squad-building-challenges\"]'))\n",
        "    )\n",
        "\n",
        "    # کلیک روی لینک SBCs\n",
        "    sbc_link.click()\n",
        "\n",
        "    # منتظر شدن تا صفحه SBCs بارگذاری شود\n",
        "    WebDriverWait(driver, 30).until(\n",
        "        EC.presence_of_element_located((By.CLASS_NAME, 'sbcc-card'))  # این کلاس را بررسی کن که درست باشد\n",
        "    )\n",
        "\n",
        "    print(\"صفحه SBCs با موفقیت بارگذاری شد.\")\n",
        "\n",
        "finally:\n",
        "    # بستن مرورگر\n",
        "    driver.quit()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 651
        },
        "id": "a2c40C0fbTmM",
        "outputId": "9f2498a7-5bdb-4fc7-a53d-441ba6bb17c7"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "error",
          "ename": "WebDriverException",
          "evalue": "Message: unknown error: cannot find Chrome binary\nStacktrace:\n#0 0x5581f08274e3 <unknown>\n#1 0x5581f0556c76 <unknown>\n#2 0x5581f057d757 <unknown>\n#3 0x5581f057c029 <unknown>\n#4 0x5581f05baccc <unknown>\n#5 0x5581f05ba47f <unknown>\n#6 0x5581f05b1de3 <unknown>\n#7 0x5581f05872dd <unknown>\n#8 0x5581f058834e <unknown>\n#9 0x5581f07e73e4 <unknown>\n#10 0x5581f07eb3d7 <unknown>\n#11 0x5581f07f5b20 <unknown>\n#12 0x5581f07ec023 <unknown>\n#13 0x5581f07ba1aa <unknown>\n#14 0x5581f08106b8 <unknown>\n#15 0x5581f0810847 <unknown>\n#16 0x5581f0820243 <unknown>\n#17 0x787d2f3ecac3 <unknown>\n",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m                        Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-6-4a593b22370e>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     15\u001b[0m \u001b[0;31m# راه‌اندازی WebDriver\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     16\u001b[0m \u001b[0mservice\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mService\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mChromeDriverManager\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0minstall\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 17\u001b[0;31m \u001b[0mdriver\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     18\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     19\u001b[0m \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chrome/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     43\u001b[0m         \u001b[0moptions\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0mOptions\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     44\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 45\u001b[0;31m         super().__init__(\n\u001b[0m\u001b[1;32m     46\u001b[0m             \u001b[0mbrowser_name\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mDesiredCapabilities\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCHROME\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"browserName\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     47\u001b[0m             \u001b[0mvendor_prefix\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"goog\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chromium/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, browser_name, vendor_prefix, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     64\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     65\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 66\u001b[0;31m             \u001b[0msuper\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__init__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mexecutor\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     67\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     68\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mquit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, command_executor, keep_alive, file_detector, options, locator_converter, web_element_cls, client_config)\u001b[0m\n\u001b[1;32m    248\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_authenticator_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    249\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_client\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 250\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_session\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    251\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_fedcm\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mFedCM\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    252\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mstart_session\u001b[0;34m(self, capabilities)\u001b[0m\n\u001b[1;32m    340\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    341\u001b[0m         \u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_create_caps\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 342\u001b[0;31m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mCommand\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mNEW_SESSION\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcaps\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    343\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msession_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"sessionId\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    344\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"capabilities\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, driver_command, params)\u001b[0m\n\u001b[1;32m    427\u001b[0m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    428\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 429\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    430\u001b[0m             \u001b[0mresponse\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_unwrap_value\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    431\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/errorhandler.py\u001b[0m in \u001b[0;36mcheck_response\u001b[0;34m(self, response)\u001b[0m\n\u001b[1;32m    230\u001b[0m                 \u001b[0malert_text\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"alert\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"text\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    231\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0malert_text\u001b[0m\u001b[0;34m)\u001b[0m  \u001b[0;31m# type: ignore[call-arg]  # mypy is not smart enough here\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 232\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m: Message: unknown error: cannot find Chrome binary\nStacktrace:\n#0 0x5581f08274e3 <unknown>\n#1 0x5581f0556c76 <unknown>\n#2 0x5581f057d757 <unknown>\n#3 0x5581f057c029 <unknown>\n#4 0x5581f05baccc <unknown>\n#5 0x5581f05ba47f <unknown>\n#6 0x5581f05b1de3 <unknown>\n#7 0x5581f05872dd <unknown>\n#8 0x5581f058834e <unknown>\n#9 0x5581f07e73e4 <unknown>\n#10 0x5581f07eb3d7 <unknown>\n#11 0x5581f07f5b20 <unknown>\n#12 0x5581f07ec023 <unknown>\n#13 0x5581f07ba1aa <unknown>\n#14 0x5581f08106b8 <unknown>\n#15 0x5581f0810847 <unknown>\n#16 0x5581f0820243 <unknown>\n#17 0x787d2f3ecac3 <unknown>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "google-chrome --version\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 141
        },
        "id": "5_DjtaphbfgA",
        "outputId": "242edb38-b0bf-4fc3-ade8-1844f3908115"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "name 'google' is not defined",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-7-78362e27d10f>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mgoogle\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0mchrome\u001b[0m \u001b[0;34m-\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0mversion\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m: name 'google' is not defined"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!apt update\n",
        "!apt install -y chromium-chromedriver\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ia-sjeNLbqwT",
        "outputId": "b8bef4fd-7d91-4d53-fc2b-8a9f9158c48f"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[33m\r0% [Working]\u001b[0m\r            \rGet:1 https://cloud.r-project.org/bin/linux/ubuntu jammy-cran40/ InRelease [3,632 B]\n",
            "\u001b[33m\r0% [Connecting to archive.ubuntu.com (91.189.91.83)] [Connecting to security.ubuntu.com (185.125.190\u001b[0m\u001b[33m\r0% [Connecting to archive.ubuntu.com (91.189.91.83)] [Connecting to security.ubuntu.com (185.125.190\u001b[0m\r                                                                                                    \rGet:2 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64  InRelease [1,581 B]\n",
            "Get:3 https://r2u.stat.illinois.edu/ubuntu jammy InRelease [6,555 B]\n",
            "Get:4 http://security.ubuntu.com/ubuntu jammy-security InRelease [129 kB]\n",
            "Hit:5 http://archive.ubuntu.com/ubuntu jammy InRelease\n",
            "Get:6 http://archive.ubuntu.com/ubuntu jammy-updates InRelease [128 kB]\n",
            "Get:7 http://archive.ubuntu.com/ubuntu jammy-backports InRelease [127 kB]\n",
            "Get:8 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64  Packages [1,370 kB]\n",
            "Hit:9 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy InRelease\n",
            "Hit:10 https://ppa.launchpadcontent.net/graphics-drivers/ppa/ubuntu jammy InRelease\n",
            "Hit:11 https://ppa.launchpadcontent.net/ubuntugis/ppa/ubuntu jammy InRelease\n",
            "Get:12 https://r2u.stat.illinois.edu/ubuntu jammy/main amd64 Packages [2,668 kB]\n",
            "Get:13 https://r2u.stat.illinois.edu/ubuntu jammy/main all Packages [8,731 kB]\n",
            "Get:14 http://archive.ubuntu.com/ubuntu jammy-updates/universe amd64 Packages [1,533 kB]\n",
            "Get:15 http://archive.ubuntu.com/ubuntu jammy-updates/restricted amd64 Packages [3,947 kB]\n",
            "Get:16 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 Packages [2,995 kB]\n",
            "Get:17 http://security.ubuntu.com/ubuntu jammy-security/main amd64 Packages [2,682 kB]\n",
            "Get:18 http://security.ubuntu.com/ubuntu jammy-security/universe amd64 Packages [1,235 kB]\n",
            "Fetched 25.6 MB in 3s (8,405 kB/s)\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "31 packages can be upgraded. Run 'apt list --upgradable' to see them.\n",
            "\u001b[1;33mW: \u001b[0mSkipping acquire of configured file 'main/source/Sources' as repository 'https://r2u.stat.illinois.edu/ubuntu jammy InRelease' does not seem to provide it (sources.list entry misspelt?)\u001b[0m\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "The following additional packages will be installed:\n",
            "  apparmor chromium-browser libfuse3-3 liblzo2-2 snapd squashfs-tools systemd-hwe-hwdb udev\n",
            "Suggested packages:\n",
            "  apparmor-profiles-extra apparmor-utils fuse3 zenity | kdialog\n",
            "The following NEW packages will be installed:\n",
            "  apparmor chromium-browser chromium-chromedriver libfuse3-3 liblzo2-2 snapd squashfs-tools\n",
            "  systemd-hwe-hwdb udev\n",
            "0 upgraded, 9 newly installed, 0 to remove and 31 not upgraded.\n",
            "Need to get 30.3 MB of archives.\n",
            "After this operation, 123 MB of additional disk space will be used.\n",
            "Get:1 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 apparmor amd64 3.0.4-2ubuntu2.4 [598 kB]\n",
            "Get:2 http://archive.ubuntu.com/ubuntu jammy/main amd64 liblzo2-2 amd64 2.10-2build3 [53.7 kB]\n",
            "Get:3 http://archive.ubuntu.com/ubuntu jammy/main amd64 squashfs-tools amd64 1:4.5-3build1 [159 kB]\n",
            "Get:4 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 udev amd64 249.11-0ubuntu3.12 [1,557 kB]\n",
            "Get:5 http://archive.ubuntu.com/ubuntu jammy/main amd64 libfuse3-3 amd64 3.10.5-1build1 [81.2 kB]\n",
            "Get:6 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 snapd amd64 2.67.1+22.04 [27.8 MB]\n",
            "Get:7 http://archive.ubuntu.com/ubuntu jammy-updates/universe amd64 chromium-browser amd64 1:85.0.4183.83-0ubuntu2.22.04.1 [49.2 kB]\n",
            "Get:8 http://archive.ubuntu.com/ubuntu jammy-updates/universe amd64 chromium-chromedriver amd64 1:85.0.4183.83-0ubuntu2.22.04.1 [2,308 B]\n",
            "Get:9 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 systemd-hwe-hwdb all 249.11.5 [3,228 B]\n",
            "Fetched 30.3 MB in 2s (14.4 MB/s)\n",
            "Preconfiguring packages ...\n",
            "Selecting previously unselected package apparmor.\n",
            "(Reading database ... 124947 files and directories currently installed.)\n",
            "Preparing to unpack .../0-apparmor_3.0.4-2ubuntu2.4_amd64.deb ...\n",
            "Unpacking apparmor (3.0.4-2ubuntu2.4) ...\n",
            "Selecting previously unselected package liblzo2-2:amd64.\n",
            "Preparing to unpack .../1-liblzo2-2_2.10-2build3_amd64.deb ...\n",
            "Unpacking liblzo2-2:amd64 (2.10-2build3) ...\n",
            "Selecting previously unselected package squashfs-tools.\n",
            "Preparing to unpack .../2-squashfs-tools_1%3a4.5-3build1_amd64.deb ...\n",
            "Unpacking squashfs-tools (1:4.5-3build1) ...\n",
            "Selecting previously unselected package udev.\n",
            "Preparing to unpack .../3-udev_249.11-0ubuntu3.12_amd64.deb ...\n",
            "Unpacking udev (249.11-0ubuntu3.12) ...\n",
            "Selecting previously unselected package libfuse3-3:amd64.\n",
            "Preparing to unpack .../4-libfuse3-3_3.10.5-1build1_amd64.deb ...\n",
            "Unpacking libfuse3-3:amd64 (3.10.5-1build1) ...\n",
            "Selecting previously unselected package snapd.\n",
            "Preparing to unpack .../5-snapd_2.67.1+22.04_amd64.deb ...\n",
            "Unpacking snapd (2.67.1+22.04) ...\n",
            "Setting up apparmor (3.0.4-2ubuntu2.4) ...\n",
            "Created symlink /etc/systemd/system/sysinit.target.wants/apparmor.service → /lib/systemd/system/apparmor.service.\n",
            "Setting up liblzo2-2:amd64 (2.10-2build3) ...\n",
            "Setting up squashfs-tools (1:4.5-3build1) ...\n",
            "Setting up udev (249.11-0ubuntu3.12) ...\n",
            "invoke-rc.d: could not determine current runlevel\n",
            "invoke-rc.d: policy-rc.d denied execution of start.\n",
            "Setting up libfuse3-3:amd64 (3.10.5-1build1) ...\n",
            "Setting up snapd (2.67.1+22.04) ...\n",
            "Created symlink /etc/systemd/system/multi-user.target.wants/snapd.apparmor.service → /lib/systemd/system/snapd.apparmor.service.\n",
            "Created symlink /etc/systemd/system/multi-user.target.wants/snapd.autoimport.service → /lib/systemd/system/snapd.autoimport.service.\n",
            "Created symlink /etc/systemd/system/multi-user.target.wants/snapd.core-fixup.service → /lib/systemd/system/snapd.core-fixup.service.\n",
            "Created symlink /etc/systemd/system/multi-user.target.wants/snapd.recovery-chooser-trigger.service → /lib/systemd/system/snapd.recovery-chooser-trigger.service.\n",
            "Created symlink /etc/systemd/system/multi-user.target.wants/snapd.seeded.service → /lib/systemd/system/snapd.seeded.service.\n",
            "Created symlink /etc/systemd/system/cloud-final.service.wants/snapd.seeded.service → /lib/systemd/system/snapd.seeded.service.\n",
            "Unit /lib/systemd/system/snapd.seeded.service is added as a dependency to a non-existent unit cloud-final.service.\n",
            "Created symlink /etc/systemd/system/multi-user.target.wants/snapd.service → /lib/systemd/system/snapd.service.\n",
            "Created symlink /etc/systemd/system/timers.target.wants/snapd.snap-repair.timer → /lib/systemd/system/snapd.snap-repair.timer.\n",
            "Created symlink /etc/systemd/system/sockets.target.wants/snapd.socket → /lib/systemd/system/snapd.socket.\n",
            "Created symlink /etc/systemd/system/final.target.wants/snapd.system-shutdown.service → /lib/systemd/system/snapd.system-shutdown.service.\n",
            "Selecting previously unselected package chromium-browser.\n",
            "(Reading database ... 125384 files and directories currently installed.)\n",
            "Preparing to unpack .../chromium-browser_1%3a85.0.4183.83-0ubuntu2.22.04.1_amd64.deb ...\n",
            "=> Installing the chromium snap\n",
            "==> Checking connectivity with the snap store\n",
            "===> System doesn't have a working snapd, skipping\n",
            "Unpacking chromium-browser (1:85.0.4183.83-0ubuntu2.22.04.1) ...\n",
            "Selecting previously unselected package chromium-chromedriver.\n",
            "Preparing to unpack .../chromium-chromedriver_1%3a85.0.4183.83-0ubuntu2.22.04.1_amd64.deb ...\n",
            "Unpacking chromium-chromedriver (1:85.0.4183.83-0ubuntu2.22.04.1) ...\n",
            "Selecting previously unselected package systemd-hwe-hwdb.\n",
            "Preparing to unpack .../systemd-hwe-hwdb_249.11.5_all.deb ...\n",
            "Unpacking systemd-hwe-hwdb (249.11.5) ...\n",
            "Setting up systemd-hwe-hwdb (249.11.5) ...\n",
            "Setting up chromium-browser (1:85.0.4183.83-0ubuntu2.22.04.1) ...\n",
            "update-alternatives: using /usr/bin/chromium-browser to provide /usr/bin/x-www-browser (x-www-browser) in auto mode\n",
            "update-alternatives: using /usr/bin/chromium-browser to provide /usr/bin/gnome-www-browser (gnome-www-browser) in auto mode\n",
            "Setting up chromium-chromedriver (1:85.0.4183.83-0ubuntu2.22.04.1) ...\n",
            "Processing triggers for udev (249.11-0ubuntu3.12) ...\n",
            "Processing triggers for mailcap (3.70+nmu1ubuntu1) ...\n",
            "Processing triggers for hicolor-icon-theme (0.17-2) ...\n",
            "Processing triggers for libc-bin (2.35-0ubuntu3.8) ...\n",
            "/sbin/ldconfig.real: /usr/local/lib/libur_adapter_level_zero.so.0 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtbbmalloc.so.2 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libhwloc.so.15 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtcm.so.1 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtbb.so.12 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtbbbind_2_5.so.3 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libur_adapter_opencl.so.0 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtbbmalloc_proxy.so.2 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libur_loader.so.0 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libumf.so.0 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtbbbind_2_0.so.3 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtbbbind.so.3 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtcm_debug.so.1 is not a symbolic link\n",
            "\n",
            "Processing triggers for man-db (2.10.2-1) ...\n",
            "Processing triggers for dbus (1.12.20-2ubuntu4.1) ...\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "\n",
        "# تنظیم مسیر Chrome و WebDriver\n",
        "os.environ[\"PATH\"] += os.pathsep + \"/usr/lib/chromium-browser/\"\n",
        "os.environ[\"PATH\"] += os.pathsep + \"/usr/bin/chromedriver\"\n"
      ],
      "metadata": {
        "id": "YxO3ek2Ab1DZ"
      },
      "execution_count": 9,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "\n",
        "options = Options()\n",
        "options.add_argument(\"--headless\")  # اجرای کروم بدون رابط گرافیکی\n",
        "options.add_argument(\"--no-sandbox\")\n",
        "options.add_argument(\"--disable-dev-shm-usage\")\n",
        "\n",
        "driver = webdriver.Chrome(options=options)\n",
        "\n",
        "# تست باز کردن سایت گوگل\n",
        "driver.get(\"https://www.google.com\")\n",
        "print(\"Chrome is working!\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MmRnjzHhb3S_",
        "outputId": "8cb0f8d3-53b3-409c-e616-d0517c31a6e6"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Chrome is working!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from selenium.webdriver.common.by import By\n",
        "from selenium.webdriver.support.ui import WebDriverWait\n",
        "from selenium.webdriver.support import expected_conditions as EC\n",
        "\n",
        "# باز کردن سایت\n",
        "driver.get(\"https://www.futbin.com/\")\n",
        "\n",
        "# منتظر می‌مانیم تا صفحه کامل بارگذاری شود و عنصر مورد نظر پیدا شود\n",
        "WebDriverWait(driver, 30).until(\n",
        "    EC.presence_of_element_located((By.CLASS_NAME, 'nav-link'))  # پیدا کردن لینک های منو در سایت\n",
        ")\n",
        "\n",
        "# چاپ اطلاعات منو (برای تست)\n",
        "links = driver.find_elements(By.CLASS_NAME, 'nav-link')  # همه لینک‌های منو\n",
        "for link in links:\n",
        "    print(link.text)  # نمایش متن لینک‌ها\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 679
        },
        "id": "iIb48CS8cEdb",
        "outputId": "79342760-8dbb-4f43-9a99-5765c944764f"
      },
      "execution_count": 11,
      "outputs": [
        {
          "ename": "TimeoutException",
          "evalue": "Message: \nStacktrace:\n#0 0x5c6fa3736a1a <unknown>\n#1 0x5c6fa31ee390 <unknown>\n#2 0x5c6fa323fc85 <unknown>\n#3 0x5c6fa323feb1 <unknown>\n#4 0x5c6fa328ed64 <unknown>\n#5 0x5c6fa3265bfd <unknown>\n#6 0x5c6fa328c07b <unknown>\n#7 0x5c6fa32659a3 <unknown>\n#8 0x5c6fa323160e <unknown>\n#9 0x5c6fa3232dd1 <unknown>\n#10 0x5c6fa36fcddb <unknown>\n#11 0x5c6fa3700cbc <unknown>\n#12 0x5c6fa36e4392 <unknown>\n#13 0x5c6fa3701834 <unknown>\n#14 0x5c6fa36c81ef <unknown>\n#15 0x5c6fa3725038 <unknown>\n#16 0x5c6fa3725216 <unknown>\n#17 0x5c6fa3735896 <unknown>\n#18 0x7c5581422ac3 <unknown>\n",
          "output_type": "error",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTimeoutException\u001b[0m                          Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-11-7ea35ee28b1d>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      7\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      8\u001b[0m \u001b[0;31m# منتظر می‌مانیم تا صفحه کامل بارگذاری شود و عنصر مورد نظر پیدا شود\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 9\u001b[0;31m WebDriverWait(driver, 30).until(\n\u001b[0m\u001b[1;32m     10\u001b[0m     \u001b[0mEC\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpresence_of_element_located\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mBy\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCLASS_NAME\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'nav-link'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m  \u001b[0;31m# پیدا کردن لینک های منو در سایت\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     11\u001b[0m )\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/support/wait.py\u001b[0m in \u001b[0;36muntil\u001b[0;34m(self, method, message)\u001b[0m\n\u001b[1;32m    144\u001b[0m                 \u001b[0;32mbreak\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    145\u001b[0m             \u001b[0mtime\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msleep\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_poll\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 146\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mTimeoutException\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    147\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    148\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0muntil_not\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmethod\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mCallable\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mD\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mT\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmessage\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mstr\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m\"\"\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m->\u001b[0m \u001b[0mUnion\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mT\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mLiteral\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mTimeoutException\u001b[0m: Message: \nStacktrace:\n#0 0x5c6fa3736a1a <unknown>\n#1 0x5c6fa31ee390 <unknown>\n#2 0x5c6fa323fc85 <unknown>\n#3 0x5c6fa323feb1 <unknown>\n#4 0x5c6fa328ed64 <unknown>\n#5 0x5c6fa3265bfd <unknown>\n#6 0x5c6fa328c07b <unknown>\n#7 0x5c6fa32659a3 <unknown>\n#8 0x5c6fa323160e <unknown>\n#9 0x5c6fa3232dd1 <unknown>\n#10 0x5c6fa36fcddb <unknown>\n#11 0x5c6fa3700cbc <unknown>\n#12 0x5c6fa36e4392 <unknown>\n#13 0x5c6fa3701834 <unknown>\n#14 0x5c6fa36c81ef <unknown>\n#15 0x5c6fa3725038 <unknown>\n#16 0x5c6fa3725216 <unknown>\n#17 0x5c6fa3735896 <unknown>\n#18 0x7c5581422ac3 <unknown>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# نصب Selenium و WebDriver برای استفاده از کروم در گوگل کلااب\n",
        "!pip install selenium\n",
        "!apt-get update # آپدیت مخازن برای دانلود کروم و وابستگی‌ها\n",
        "!apt-get install -y chromium-chromedriver\n",
        "!pip install webdriver-manager\n",
        "\n",
        "# تنظیمات کروم برای استفاده از Selenium در Google Colab\n",
        "import sys\n",
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "from webdriver_manager.chrome import ChromeDriverManager\n",
        "\n",
        "# تنظیمات Chrome\n",
        "options = Options()\n",
        "options.add_argument('--headless')  # بدون نمایش صفحه مرورگر\n",
        "options.add_argument('--no-sandbox')\n",
        "options.add_argument('--disable-dev-shm-usage')\n",
        "\n",
        "# راه‌اندازی WebDriver\n",
        "service = Service(ChromeDriverManager().install())\n",
        "driver = webdriver.Chrome(service=service, options=options)\n",
        "\n",
        "# باز کردن سایت\n",
        "driver.get(\"https://www.futbin.com/\")\n",
        "\n",
        "# ۴. استخراج داده‌ها (منتظر می‌مانیم تا یک عنصر خاص در صفحه بارگذاری شود)\n",
        "from selenium.webdriver.common.by import By\n",
        "from selenium.webdriver.support.ui import WebDriverWait\n",
        "from selenium.webdriver.support import expected_conditions as EC\n",
        "\n",
        "# منتظر می‌مانیم تا عنصر مربوطه در صفحه ظاهر شود\n",
        "WebDriverWait(driver, 30).until(\n",
        "    EC.presence_of_element_located((By.CLASS_NAME, 'nav-link'))  # به دنبال لینک‌ها می‌گردیم\n",
        ")\n",
        "\n",
        "# ۵. تعامل با صفحه و استخراج داده‌ها\n",
        "# پیدا کردن تمام لینک‌ها با کلاس 'nav-link'\n",
        "links = driver.find_elements(By.CLASS_NAME, 'nav-link')\n",
        "\n",
        "# چاپ همه لینک‌ها\n",
        "print(\"تمام لینک‌های موجود در منو:\")\n",
        "for link in links:\n",
        "    print(link.text)  # نمایش نام لینک‌ها\n",
        "\n",
        "# ۵. تعامل با یک دکمه (در صورتی که بخواهید دکمه‌ای را کلیک کنید)\n",
        "# این فقط یک مثال است که با توجه به سایت، می‌توانید آن را تغییر دهید\n",
        "try:\n",
        "    # فرض می‌کنیم که دکمه‌ای با کلاس خاص وجود دارد که می‌خواهیم روی آن کلیک کنیم\n",
        "    button = driver.find_element(By.XPATH, \"//a[@href='/squad-building-challenges']\")  # لینک SBCs\n",
        "    button.click()  # کلیک روی دکمه\n",
        "    print(\"روی دکمه کلیک شد.\")\n",
        "except Exception as e:\n",
        "    print(f\"خطا در پیدا کردن یا کلیک روی دکمه: {e}\")\n",
        "\n",
        "# ۶. بستن WebDriver پس از اتمام کار\n",
        "driver.quit()  # بستن WebDriver پس از پایان کار\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "ZkY6tDRJcYaT",
        "outputId": "a5f32028-ba2d-4aab-bbaf-911157ae904b"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: selenium in /usr/local/lib/python3.11/dist-packages (4.29.0)\n",
            "Requirement already satisfied: urllib3<3,>=1.26 in /usr/local/lib/python3.11/dist-packages (from urllib3[socks]<3,>=1.26->selenium) (2.3.0)\n",
            "Requirement already satisfied: trio~=0.17 in /usr/local/lib/python3.11/dist-packages (from selenium) (0.29.0)\n",
            "Requirement already satisfied: trio-websocket~=0.9 in /usr/local/lib/python3.11/dist-packages (from selenium) (0.12.2)\n",
            "Requirement already satisfied: certifi>=2021.10.8 in /usr/local/lib/python3.11/dist-packages (from selenium) (2025.1.31)\n",
            "Requirement already satisfied: typing_extensions~=4.9 in /usr/local/lib/python3.11/dist-packages (from selenium) (4.12.2)\n",
            "Requirement already satisfied: websocket-client~=1.8 in /usr/local/lib/python3.11/dist-packages (from selenium) (1.8.0)\n",
            "Requirement already satisfied: attrs>=23.2.0 in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (25.1.0)\n",
            "Requirement already satisfied: sortedcontainers in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (2.4.0)\n",
            "Requirement already satisfied: idna in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (3.10)\n",
            "Requirement already satisfied: outcome in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (1.3.0.post0)\n",
            "Requirement already satisfied: sniffio>=1.3.0 in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (1.3.1)\n",
            "Requirement already satisfied: wsproto>=0.14 in /usr/local/lib/python3.11/dist-packages (from trio-websocket~=0.9->selenium) (1.2.0)\n",
            "Requirement already satisfied: pysocks!=1.5.7,<2.0,>=1.5.6 in /usr/local/lib/python3.11/dist-packages (from urllib3[socks]<3,>=1.26->selenium) (1.7.1)\n",
            "Requirement already satisfied: h11<1,>=0.9.0 in /usr/local/lib/python3.11/dist-packages (from wsproto>=0.14->trio-websocket~=0.9->selenium) (0.14.0)\n",
            "Hit:1 https://cloud.r-project.org/bin/linux/ubuntu jammy-cran40/ InRelease\n",
            "Hit:2 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64  InRelease\n",
            "Hit:3 https://r2u.stat.illinois.edu/ubuntu jammy InRelease\n",
            "Hit:4 http://security.ubuntu.com/ubuntu jammy-security InRelease\n",
            "Hit:5 http://archive.ubuntu.com/ubuntu jammy InRelease\n",
            "Hit:6 http://archive.ubuntu.com/ubuntu jammy-updates InRelease\n",
            "Hit:7 http://archive.ubuntu.com/ubuntu jammy-backports InRelease\n",
            "Hit:8 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy InRelease\n",
            "Hit:9 https://ppa.launchpadcontent.net/graphics-drivers/ppa/ubuntu jammy InRelease\n",
            "Hit:10 https://ppa.launchpadcontent.net/ubuntugis/ppa/ubuntu jammy InRelease\n",
            "Reading package lists... Done\n",
            "W: Skipping acquire of configured file 'main/source/Sources' as repository 'https://r2u.stat.illinois.edu/ubuntu jammy InRelease' does not seem to provide it (sources.list entry misspelt?)\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "chromium-chromedriver is already the newest version (1:85.0.4183.83-0ubuntu2.22.04.1).\n",
            "0 upgraded, 0 newly installed, 0 to remove and 31 not upgraded.\n",
            "Requirement already satisfied: webdriver-manager in /usr/local/lib/python3.11/dist-packages (4.0.2)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.11/dist-packages (from webdriver-manager) (2.32.3)\n",
            "Requirement already satisfied: python-dotenv in /usr/local/lib/python3.11/dist-packages (from webdriver-manager) (1.0.1)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.11/dist-packages (from webdriver-manager) (24.2)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests->webdriver-manager) (3.4.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests->webdriver-manager) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests->webdriver-manager) (2.3.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests->webdriver-manager) (2025.1.31)\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "WebDriverException",
          "evalue": "Message: unknown error: Chrome failed to start: exited abnormally.\n  (unknown error: DevToolsActivePort file doesn't exist)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x5ba0951024e3 <unknown>\n#1 0x5ba094e31c76 <unknown>\n#2 0x5ba094e5ad78 <unknown>\n#3 0x5ba094e57029 <unknown>\n#4 0x5ba094e95ccc <unknown>\n#5 0x5ba094e9547f <unknown>\n#6 0x5ba094e8cde3 <unknown>\n#7 0x5ba094e622dd <unknown>\n#8 0x5ba094e6334e <unknown>\n#9 0x5ba0950c23e4 <unknown>\n#10 0x5ba0950c63d7 <unknown>\n#11 0x5ba0950d0b20 <unknown>\n#12 0x5ba0950c7023 <unknown>\n#13 0x5ba0950951aa <unknown>\n#14 0x5ba0950eb6b8 <unknown>\n#15 0x5ba0950eb847 <unknown>\n#16 0x5ba0950fb243 <unknown>\n#17 0x7f5ad9877ac3 <unknown>\n",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m                        Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-12-8b3042c43c1f>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     20\u001b[0m \u001b[0;31m# راه‌اندازی WebDriver\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     21\u001b[0m \u001b[0mservice\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mService\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mChromeDriverManager\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0minstall\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 22\u001b[0;31m \u001b[0mdriver\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     23\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     24\u001b[0m \u001b[0;31m# باز کردن سایت\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chrome/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     43\u001b[0m         \u001b[0moptions\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0mOptions\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     44\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 45\u001b[0;31m         super().__init__(\n\u001b[0m\u001b[1;32m     46\u001b[0m             \u001b[0mbrowser_name\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mDesiredCapabilities\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCHROME\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"browserName\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     47\u001b[0m             \u001b[0mvendor_prefix\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"goog\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chromium/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, browser_name, vendor_prefix, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     64\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     65\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 66\u001b[0;31m             \u001b[0msuper\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__init__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mexecutor\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     67\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     68\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mquit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, command_executor, keep_alive, file_detector, options, locator_converter, web_element_cls, client_config)\u001b[0m\n\u001b[1;32m    248\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_authenticator_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    249\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_client\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 250\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_session\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    251\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_fedcm\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mFedCM\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    252\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mstart_session\u001b[0;34m(self, capabilities)\u001b[0m\n\u001b[1;32m    340\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    341\u001b[0m         \u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_create_caps\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 342\u001b[0;31m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mCommand\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mNEW_SESSION\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcaps\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    343\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msession_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"sessionId\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    344\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"capabilities\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, driver_command, params)\u001b[0m\n\u001b[1;32m    427\u001b[0m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    428\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 429\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    430\u001b[0m             \u001b[0mresponse\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_unwrap_value\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    431\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/errorhandler.py\u001b[0m in \u001b[0;36mcheck_response\u001b[0;34m(self, response)\u001b[0m\n\u001b[1;32m    230\u001b[0m                 \u001b[0malert_text\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"alert\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"text\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    231\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0malert_text\u001b[0m\u001b[0;34m)\u001b[0m  \u001b[0;31m# type: ignore[call-arg]  # mypy is not smart enough here\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 232\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m: Message: unknown error: Chrome failed to start: exited abnormally.\n  (unknown error: DevToolsActivePort file doesn't exist)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x5ba0951024e3 <unknown>\n#1 0x5ba094e31c76 <unknown>\n#2 0x5ba094e5ad78 <unknown>\n#3 0x5ba094e57029 <unknown>\n#4 0x5ba094e95ccc <unknown>\n#5 0x5ba094e9547f <unknown>\n#6 0x5ba094e8cde3 <unknown>\n#7 0x5ba094e622dd <unknown>\n#8 0x5ba094e6334e <unknown>\n#9 0x5ba0950c23e4 <unknown>\n#10 0x5ba0950c63d7 <unknown>\n#11 0x5ba0950d0b20 <unknown>\n#12 0x5ba0950c7023 <unknown>\n#13 0x5ba0950951aa <unknown>\n#14 0x5ba0950eb6b8 <unknown>\n#15 0x5ba0950eb847 <unknown>\n#16 0x5ba0950fb243 <unknown>\n#17 0x7f5ad9877ac3 <unknown>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# نصب Selenium و WebDriver برای استفاده از کروم در گوگل کلااب\n",
        "!pip install selenium\n",
        "!apt-get update # آپدیت مخازن برای دانلود کروم و وابستگی‌ها\n",
        "!apt-get install -y chromium-chromedriver\n",
        "!pip install webdriver-manager\n",
        "\n",
        "# تنظیمات کروم برای استفاده از Selenium در Google Colab\n",
        "import sys\n",
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "from webdriver_manager.chrome import ChromeDriverManager\n",
        "\n",
        "# تنظیمات Chrome\n",
        "options = Options()\n",
        "options.add_argument('--headless')  # بدون نمایش صفحه مرورگر\n",
        "options.add_argument('--no-sandbox')\n",
        "options.add_argument('--disable-dev-shm-usage')\n",
        "options.add_argument('--remote-debugging-port=9222')  # تنظیم برای جلوگیری از خطاهای کروم\n",
        "\n",
        "# راه‌اندازی WebDriver\n",
        "service = Service(ChromeDriverManager().install())\n",
        "driver = webdriver.Chrome(service=service, options=options)\n",
        "\n",
        "# باز کردن سایت\n",
        "driver.get(\"https://www.futbin.com/\")\n",
        "\n",
        "# ۴. استخراج داده‌ها (منتظر می‌مانیم تا یک عنصر خاص در صفحه بارگذاری شود)\n",
        "from selenium.webdriver.common.by import By\n",
        "from selenium.webdriver.support.ui import WebDriverWait\n",
        "from selenium.webdriver.support import expected_conditions as EC\n",
        "\n",
        "# منتظر می‌مانیم تا عنصر مربوطه در صفحه ظاهر شود\n",
        "WebDriverWait(driver, 30).until(\n",
        "    EC.presence_of_element_located((By.CLASS_NAME, 'nav-link'))  # به دنبال لینک‌ها می‌گردیم\n",
        ")\n",
        "\n",
        "# ۵. تعامل با صفحه و استخراج داده‌ها\n",
        "# پیدا کردن تمام لینک‌ها با کلاس 'nav-link'\n",
        "links = driver.find_elements(By.CLASS_NAME, 'nav-link')\n",
        "\n",
        "# چاپ همه لینک‌ها\n",
        "print(\"تمام لینک‌های موجود در منو:\")\n",
        "for link in links:\n",
        "    print(link.text)  # نمایش نام لینک‌ها\n",
        "\n",
        "# ۵. تعامل با یک دکمه (در صورتی که بخواهید دکمه‌ای را کلیک کنید)\n",
        "# این فقط یک مثال است که با توجه به سایت، می‌توانید آن را تغییر دهید\n",
        "try:\n",
        "    # فرض می‌کنیم که دکمه‌ای با کلاس خاص وجود دارد که می‌خواهیم روی آن کلیک کنیم\n",
        "    button = driver.find_element(By.XPATH, \"//a[@href='/squad-building-challenges']\")  # لینک SBCs\n",
        "    button.click()  # کلیک روی دکمه\n",
        "    print(\"روی دکمه کلیک شد.\")\n",
        "except Exception as e:\n",
        "    print(f\"خطا در پیدا کردن یا کلیک روی دکمه: {e}\")\n",
        "\n",
        "# ۶. بستن WebDriver پس از اتمام کار\n",
        "driver.quit()  # بستن WebDriver پس از پایان کار\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "0VmxGMyDckpY",
        "outputId": "6294ab68-76ec-484e-9398-3baf82cbc7d8"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: selenium in /usr/local/lib/python3.11/dist-packages (4.29.0)\n",
            "Requirement already satisfied: urllib3<3,>=1.26 in /usr/local/lib/python3.11/dist-packages (from urllib3[socks]<3,>=1.26->selenium) (2.3.0)\n",
            "Requirement already satisfied: trio~=0.17 in /usr/local/lib/python3.11/dist-packages (from selenium) (0.29.0)\n",
            "Requirement already satisfied: trio-websocket~=0.9 in /usr/local/lib/python3.11/dist-packages (from selenium) (0.12.2)\n",
            "Requirement already satisfied: certifi>=2021.10.8 in /usr/local/lib/python3.11/dist-packages (from selenium) (2025.1.31)\n",
            "Requirement already satisfied: typing_extensions~=4.9 in /usr/local/lib/python3.11/dist-packages (from selenium) (4.12.2)\n",
            "Requirement already satisfied: websocket-client~=1.8 in /usr/local/lib/python3.11/dist-packages (from selenium) (1.8.0)\n",
            "Requirement already satisfied: attrs>=23.2.0 in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (25.1.0)\n",
            "Requirement already satisfied: sortedcontainers in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (2.4.0)\n",
            "Requirement already satisfied: idna in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (3.10)\n",
            "Requirement already satisfied: outcome in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (1.3.0.post0)\n",
            "Requirement already satisfied: sniffio>=1.3.0 in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (1.3.1)\n",
            "Requirement already satisfied: wsproto>=0.14 in /usr/local/lib/python3.11/dist-packages (from trio-websocket~=0.9->selenium) (1.2.0)\n",
            "Requirement already satisfied: pysocks!=1.5.7,<2.0,>=1.5.6 in /usr/local/lib/python3.11/dist-packages (from urllib3[socks]<3,>=1.26->selenium) (1.7.1)\n",
            "Requirement already satisfied: h11<1,>=0.9.0 in /usr/local/lib/python3.11/dist-packages (from wsproto>=0.14->trio-websocket~=0.9->selenium) (0.14.0)\n",
            "Hit:1 http://security.ubuntu.com/ubuntu jammy-security InRelease\n",
            "Hit:2 https://cloud.r-project.org/bin/linux/ubuntu jammy-cran40/ InRelease\n",
            "Hit:3 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64  InRelease\n",
            "Hit:4 https://r2u.stat.illinois.edu/ubuntu jammy InRelease\n",
            "Hit:5 http://archive.ubuntu.com/ubuntu jammy InRelease\n",
            "Hit:6 http://archive.ubuntu.com/ubuntu jammy-updates InRelease\n",
            "Hit:7 http://archive.ubuntu.com/ubuntu jammy-backports InRelease\n",
            "Hit:8 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy InRelease\n",
            "Hit:9 https://ppa.launchpadcontent.net/graphics-drivers/ppa/ubuntu jammy InRelease\n",
            "Hit:10 https://ppa.launchpadcontent.net/ubuntugis/ppa/ubuntu jammy InRelease\n",
            "Reading package lists... Done\n",
            "W: Skipping acquire of configured file 'main/source/Sources' as repository 'https://r2u.stat.illinois.edu/ubuntu jammy InRelease' does not seem to provide it (sources.list entry misspelt?)\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "chromium-chromedriver is already the newest version (1:85.0.4183.83-0ubuntu2.22.04.1).\n",
            "0 upgraded, 0 newly installed, 0 to remove and 31 not upgraded.\n",
            "Requirement already satisfied: webdriver-manager in /usr/local/lib/python3.11/dist-packages (4.0.2)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.11/dist-packages (from webdriver-manager) (2.32.3)\n",
            "Requirement already satisfied: python-dotenv in /usr/local/lib/python3.11/dist-packages (from webdriver-manager) (1.0.1)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.11/dist-packages (from webdriver-manager) (24.2)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests->webdriver-manager) (3.4.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests->webdriver-manager) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests->webdriver-manager) (2.3.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests->webdriver-manager) (2025.1.31)\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "WebDriverException",
          "evalue": "Message: unknown error: Chrome failed to start: exited abnormally.\n  (chrome not reachable)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x569138e3a4e3 <unknown>\n#1 0x569138b69c76 <unknown>\n#2 0x569138b92d78 <unknown>\n#3 0x569138b8f029 <unknown>\n#4 0x569138bcdccc <unknown>\n#5 0x569138bcd47f <unknown>\n#6 0x569138bc4de3 <unknown>\n#7 0x569138b9a2dd <unknown>\n#8 0x569138b9b34e <unknown>\n#9 0x569138dfa3e4 <unknown>\n#10 0x569138dfe3d7 <unknown>\n#11 0x569138e08b20 <unknown>\n#12 0x569138dff023 <unknown>\n#13 0x569138dcd1aa <unknown>\n#14 0x569138e236b8 <unknown>\n#15 0x569138e23847 <unknown>\n#16 0x569138e33243 <unknown>\n#17 0x7f4bdfc59ac3 <unknown>\n",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m                        Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-13-0108916b8eb2>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     21\u001b[0m \u001b[0;31m# راه‌اندازی WebDriver\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     22\u001b[0m \u001b[0mservice\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mService\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mChromeDriverManager\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0minstall\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 23\u001b[0;31m \u001b[0mdriver\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     24\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     25\u001b[0m \u001b[0;31m# باز کردن سایت\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chrome/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     43\u001b[0m         \u001b[0moptions\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0mOptions\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     44\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 45\u001b[0;31m         super().__init__(\n\u001b[0m\u001b[1;32m     46\u001b[0m             \u001b[0mbrowser_name\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mDesiredCapabilities\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCHROME\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"browserName\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     47\u001b[0m             \u001b[0mvendor_prefix\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"goog\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chromium/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, browser_name, vendor_prefix, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     64\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     65\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 66\u001b[0;31m             \u001b[0msuper\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__init__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mexecutor\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     67\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     68\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mquit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, command_executor, keep_alive, file_detector, options, locator_converter, web_element_cls, client_config)\u001b[0m\n\u001b[1;32m    248\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_authenticator_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    249\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_client\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 250\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_session\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    251\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_fedcm\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mFedCM\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    252\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mstart_session\u001b[0;34m(self, capabilities)\u001b[0m\n\u001b[1;32m    340\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    341\u001b[0m         \u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_create_caps\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 342\u001b[0;31m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mCommand\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mNEW_SESSION\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcaps\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    343\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msession_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"sessionId\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    344\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"capabilities\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, driver_command, params)\u001b[0m\n\u001b[1;32m    427\u001b[0m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    428\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 429\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    430\u001b[0m             \u001b[0mresponse\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_unwrap_value\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    431\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/errorhandler.py\u001b[0m in \u001b[0;36mcheck_response\u001b[0;34m(self, response)\u001b[0m\n\u001b[1;32m    230\u001b[0m                 \u001b[0malert_text\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"alert\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"text\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    231\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0malert_text\u001b[0m\u001b[0;34m)\u001b[0m  \u001b[0;31m# type: ignore[call-arg]  # mypy is not smart enough here\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 232\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m: Message: unknown error: Chrome failed to start: exited abnormally.\n  (chrome not reachable)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x569138e3a4e3 <unknown>\n#1 0x569138b69c76 <unknown>\n#2 0x569138b92d78 <unknown>\n#3 0x569138b8f029 <unknown>\n#4 0x569138bcdccc <unknown>\n#5 0x569138bcd47f <unknown>\n#6 0x569138bc4de3 <unknown>\n#7 0x569138b9a2dd <unknown>\n#8 0x569138b9b34e <unknown>\n#9 0x569138dfa3e4 <unknown>\n#10 0x569138dfe3d7 <unknown>\n#11 0x569138e08b20 <unknown>\n#12 0x569138dff023 <unknown>\n#13 0x569138dcd1aa <unknown>\n#14 0x569138e236b8 <unknown>\n#15 0x569138e23847 <unknown>\n#16 0x569138e33243 <unknown>\n#17 0x7f4bdfc59ac3 <unknown>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# نصب وابستگی‌ها\n",
        "!apt-get update # به‌روزرسانی مخازن\n",
        "!apt-get install -y chromium-chromedriver\n",
        "!pip install selenium\n",
        "!pip install webdriver-manager\n",
        "\n",
        "# تنظیمات Selenium برای استفاده از کروم در Google Colab\n",
        "import sys\n",
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "from webdriver_manager.chrome import ChromeDriverManager\n",
        "\n",
        "# تنظیمات کروم در حالت headless\n",
        "options = Options()\n",
        "options.add_argument('--headless')  # حالت بدون رابط گرافیکی\n",
        "options.add_argument('--no-sandbox')  # برای جلوگیری از مشکلات sandbox\n",
        "options.add_argument('--disable-dev-shm-usage')  # برای بهبود عملکرد در محیط‌های مجازی\n",
        "options.add_argument('--remote-debugging-port=9222')  # جلوگیری از خطاهای مربوط به اتصال کروم\n",
        "\n",
        "# راه‌اندازی ChromeDriver\n",
        "service = Service(ChromeDriverManager().install())\n",
        "driver = webdriver.Chrome(service=service, options=options)\n",
        "\n",
        "# باز کردن سایت مورد نظر\n",
        "driver.get(\"https://www.futbin.com/\")\n",
        "\n",
        "# ۴. استخراج داده‌ها (منتظر می‌مانیم تا یک عنصر خاص در صفحه بارگذاری شود)\n",
        "from selenium.webdriver.common.by import By\n",
        "from selenium.webdriver.support.ui import WebDriverWait\n",
        "from selenium.webdriver.support import expected_conditions as EC\n",
        "\n",
        "# منتظر می‌مانیم تا عنصر خاصی در صفحه ظاهر شود (در اینجا، لینک‌ها)\n",
        "WebDriverWait(driver, 30).until(\n",
        "    EC.presence_of_element_located((By.CLASS_NAME, 'nav-link'))  # به دنبال لینک‌ها می‌گردیم\n",
        ")\n",
        "\n",
        "# ۵. استخراج لینک‌ها از صفحه\n",
        "links = driver.find_elements(By.CLASS_NAME, 'nav-link')\n",
        "\n",
        "# چاپ تمام لینک‌ها\n",
        "print(\"تمام لینک‌های موجود در منو:\")\n",
        "for link in links:\n",
        "    print(link.text)\n",
        "\n",
        "# ۶. بستن WebDriver پس از اتمام کار\n",
        "driver.quit()  # بستن WebDriver پس از پایان کار\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "YMHOolytcvn0",
        "outputId": "b375dd77-4f68-4efe-cd9d-a6ebc9df5e8d"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\r0% [Working]\r            \rHit:1 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64  InRelease\n",
            "\r0% [Connecting to archive.ubuntu.com (185.125.190.83)] [Waiting for headers] [Connected to cloud.r-p\r                                                                                                    \rHit:2 https://cloud.r-project.org/bin/linux/ubuntu jammy-cran40/ InRelease\n",
            "\r0% [Waiting for headers] [Waiting for headers] [Waiting for headers] [Connected to ppa.launchpadcont\r0% [Waiting for headers] [Waiting for headers] [Waiting for headers] [Connected to ppa.launchpadcont\r                                                                                                    \rHit:3 https://r2u.stat.illinois.edu/ubuntu jammy InRelease\n",
            "Hit:4 http://archive.ubuntu.com/ubuntu jammy InRelease\n",
            "Hit:5 http://archive.ubuntu.com/ubuntu jammy-updates InRelease\n",
            "Hit:6 http://archive.ubuntu.com/ubuntu jammy-backports InRelease\n",
            "Hit:7 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy InRelease\n",
            "Hit:8 https://ppa.launchpadcontent.net/graphics-drivers/ppa/ubuntu jammy InRelease\n",
            "Hit:9 https://ppa.launchpadcontent.net/ubuntugis/ppa/ubuntu jammy InRelease\n",
            "Hit:10 http://security.ubuntu.com/ubuntu jammy-security InRelease\n",
            "Reading package lists... Done\n",
            "W: Skipping acquire of configured file 'main/source/Sources' as repository 'https://r2u.stat.illinois.edu/ubuntu jammy InRelease' does not seem to provide it (sources.list entry misspelt?)\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "chromium-chromedriver is already the newest version (1:85.0.4183.83-0ubuntu2.22.04.1).\n",
            "0 upgraded, 0 newly installed, 0 to remove and 31 not upgraded.\n",
            "Requirement already satisfied: selenium in /usr/local/lib/python3.11/dist-packages (4.29.0)\n",
            "Requirement already satisfied: urllib3<3,>=1.26 in /usr/local/lib/python3.11/dist-packages (from urllib3[socks]<3,>=1.26->selenium) (2.3.0)\n",
            "Requirement already satisfied: trio~=0.17 in /usr/local/lib/python3.11/dist-packages (from selenium) (0.29.0)\n",
            "Requirement already satisfied: trio-websocket~=0.9 in /usr/local/lib/python3.11/dist-packages (from selenium) (0.12.2)\n",
            "Requirement already satisfied: certifi>=2021.10.8 in /usr/local/lib/python3.11/dist-packages (from selenium) (2025.1.31)\n",
            "Requirement already satisfied: typing_extensions~=4.9 in /usr/local/lib/python3.11/dist-packages (from selenium) (4.12.2)\n",
            "Requirement already satisfied: websocket-client~=1.8 in /usr/local/lib/python3.11/dist-packages (from selenium) (1.8.0)\n",
            "Requirement already satisfied: attrs>=23.2.0 in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (25.1.0)\n",
            "Requirement already satisfied: sortedcontainers in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (2.4.0)\n",
            "Requirement already satisfied: idna in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (3.10)\n",
            "Requirement already satisfied: outcome in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (1.3.0.post0)\n",
            "Requirement already satisfied: sniffio>=1.3.0 in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (1.3.1)\n",
            "Requirement already satisfied: wsproto>=0.14 in /usr/local/lib/python3.11/dist-packages (from trio-websocket~=0.9->selenium) (1.2.0)\n",
            "Requirement already satisfied: pysocks!=1.5.7,<2.0,>=1.5.6 in /usr/local/lib/python3.11/dist-packages (from urllib3[socks]<3,>=1.26->selenium) (1.7.1)\n",
            "Requirement already satisfied: h11<1,>=0.9.0 in /usr/local/lib/python3.11/dist-packages (from wsproto>=0.14->trio-websocket~=0.9->selenium) (0.14.0)\n",
            "Requirement already satisfied: webdriver-manager in /usr/local/lib/python3.11/dist-packages (4.0.2)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.11/dist-packages (from webdriver-manager) (2.32.3)\n",
            "Requirement already satisfied: python-dotenv in /usr/local/lib/python3.11/dist-packages (from webdriver-manager) (1.0.1)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.11/dist-packages (from webdriver-manager) (24.2)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests->webdriver-manager) (3.4.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests->webdriver-manager) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests->webdriver-manager) (2.3.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests->webdriver-manager) (2025.1.31)\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "WebDriverException",
          "evalue": "Message: unknown error: Chrome failed to start: exited abnormally.\n  (chrome not reachable)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x56f54f17f4e3 <unknown>\n#1 0x56f54eeaec76 <unknown>\n#2 0x56f54eed7d78 <unknown>\n#3 0x56f54eed4029 <unknown>\n#4 0x56f54ef12ccc <unknown>\n#5 0x56f54ef1247f <unknown>\n#6 0x56f54ef09de3 <unknown>\n#7 0x56f54eedf2dd <unknown>\n#8 0x56f54eee034e <unknown>\n#9 0x56f54f13f3e4 <unknown>\n#10 0x56f54f1433d7 <unknown>\n#11 0x56f54f14db20 <unknown>\n#12 0x56f54f144023 <unknown>\n#13 0x56f54f1121aa <unknown>\n#14 0x56f54f1686b8 <unknown>\n#15 0x56f54f168847 <unknown>\n#16 0x56f54f178243 <unknown>\n#17 0x7bc03f645ac3 <unknown>\n",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m                        Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-14-e3174a28b6d9>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     21\u001b[0m \u001b[0;31m# راه‌اندازی ChromeDriver\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     22\u001b[0m \u001b[0mservice\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mService\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mChromeDriverManager\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0minstall\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 23\u001b[0;31m \u001b[0mdriver\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     24\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     25\u001b[0m \u001b[0;31m# باز کردن سایت مورد نظر\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chrome/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     43\u001b[0m         \u001b[0moptions\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0mOptions\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     44\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 45\u001b[0;31m         super().__init__(\n\u001b[0m\u001b[1;32m     46\u001b[0m             \u001b[0mbrowser_name\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mDesiredCapabilities\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCHROME\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"browserName\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     47\u001b[0m             \u001b[0mvendor_prefix\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"goog\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chromium/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, browser_name, vendor_prefix, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     64\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     65\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 66\u001b[0;31m             \u001b[0msuper\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__init__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mexecutor\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     67\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     68\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mquit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, command_executor, keep_alive, file_detector, options, locator_converter, web_element_cls, client_config)\u001b[0m\n\u001b[1;32m    248\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_authenticator_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    249\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_client\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 250\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_session\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    251\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_fedcm\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mFedCM\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    252\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mstart_session\u001b[0;34m(self, capabilities)\u001b[0m\n\u001b[1;32m    340\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    341\u001b[0m         \u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_create_caps\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 342\u001b[0;31m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mCommand\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mNEW_SESSION\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcaps\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    343\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msession_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"sessionId\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    344\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"capabilities\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, driver_command, params)\u001b[0m\n\u001b[1;32m    427\u001b[0m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    428\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 429\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    430\u001b[0m             \u001b[0mresponse\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_unwrap_value\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    431\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/errorhandler.py\u001b[0m in \u001b[0;36mcheck_response\u001b[0;34m(self, response)\u001b[0m\n\u001b[1;32m    230\u001b[0m                 \u001b[0malert_text\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"alert\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"text\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    231\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0malert_text\u001b[0m\u001b[0;34m)\u001b[0m  \u001b[0;31m# type: ignore[call-arg]  # mypy is not smart enough here\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 232\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m: Message: unknown error: Chrome failed to start: exited abnormally.\n  (chrome not reachable)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x56f54f17f4e3 <unknown>\n#1 0x56f54eeaec76 <unknown>\n#2 0x56f54eed7d78 <unknown>\n#3 0x56f54eed4029 <unknown>\n#4 0x56f54ef12ccc <unknown>\n#5 0x56f54ef1247f <unknown>\n#6 0x56f54ef09de3 <unknown>\n#7 0x56f54eedf2dd <unknown>\n#8 0x56f54eee034e <unknown>\n#9 0x56f54f13f3e4 <unknown>\n#10 0x56f54f1433d7 <unknown>\n#11 0x56f54f14db20 <unknown>\n#12 0x56f54f144023 <unknown>\n#13 0x56f54f1121aa <unknown>\n#14 0x56f54f1686b8 <unknown>\n#15 0x56f54f168847 <unknown>\n#16 0x56f54f178243 <unknown>\n#17 0x7bc03f645ac3 <unknown>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# نصب وابستگی‌ها\n",
        "!apt-get update\n",
        "!apt-get install -y chromium-chromedriver\n",
        "!pip install selenium\n",
        "!pip install webdriver-manager\n",
        "\n",
        "# تنظیمات Selenium برای استفاده از کروم در Google Colab\n",
        "import sys\n",
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "from webdriver_manager.chrome import ChromeDriverManager\n",
        "\n",
        "# تنظیمات کروم برای استفاده در محیط Google Colab\n",
        "options = Options()\n",
        "options.add_argument('--headless')  # حالت بدون رابط گرافیکی\n",
        "options.add_argument('--no-sandbox')  # برای جلوگیری از مشکلات sandbox\n",
        "options.add_argument('--disable-dev-shm-usage')  # برای بهبود عملکرد در محیط‌های مجازی\n",
        "options.add_argument('--remote-debugging-port=9222')  # برای جلوگیری از خطاهای مربوط به اتصال کروم\n",
        "options.add_argument('--disable-gpu')  # برای رفع مشکلات مربوط به استفاده از GPU\n",
        "\n",
        "# تنظیمات مسیر Chromium به صورت دستی\n",
        "options.binary_location = '/usr/bin/chromium-browser'\n",
        "\n",
        "# راه‌اندازی ChromeDriver\n",
        "service = Service(ChromeDriverManager().install())\n",
        "driver = webdriver.Chrome(service=service, options=options)\n",
        "\n",
        "# باز کردن سایت مورد نظر\n",
        "driver.get(\"https://www.futbin.com/\")\n",
        "\n",
        "# ۴. استخراج داده‌ها (منتظر می‌مانیم تا یک عنصر خاص در صفحه بارگذاری شود)\n",
        "from selenium.webdriver.common.by import By\n",
        "from selenium.webdriver.support.ui import WebDriverWait\n",
        "from selenium.webdriver.support import expected_conditions as EC\n",
        "\n",
        "# منتظر می‌مانیم تا عنصر خاصی در صفحه ظاهر شود (در اینجا، لینک‌ها)\n",
        "WebDriverWait(driver, 30).until(\n",
        "    EC.presence_of_element_located((By.CLASS_NAME, 'nav-link'))  # به دنبال لینک‌ها می‌گردیم\n",
        ")\n",
        "\n",
        "# ۵. استخراج لینک‌ها از صفحه\n",
        "links = driver.find_elements(By.CLASS_NAME, 'nav-link')\n",
        "\n",
        "# چاپ تمام لینک‌ها\n",
        "print(\"تمام لینک‌های موجود در منو:\")\n",
        "for link in links:\n",
        "    print(link.text)\n",
        "\n",
        "# ۶. بستن WebDriver پس از اتمام کار\n",
        "driver.quit()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "AIKM0-V3c9rQ",
        "outputId": "15912088-abc8-4874-874e-dd17f8611237"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\r0% [Working]\r            \rHit:1 https://cloud.r-project.org/bin/linux/ubuntu jammy-cran40/ InRelease\n",
            "\r0% [Connecting to archive.ubuntu.com (91.189.91.83)] [Connecting to security.ubuntu.com (91.189.91.8\r                                                                                                    \rHit:2 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64  InRelease\n",
            "Hit:3 https://r2u.stat.illinois.edu/ubuntu jammy InRelease\n",
            "Hit:4 http://security.ubuntu.com/ubuntu jammy-security InRelease\n",
            "Hit:5 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy InRelease\n",
            "Hit:6 https://ppa.launchpadcontent.net/graphics-drivers/ppa/ubuntu jammy InRelease\n",
            "Hit:7 https://ppa.launchpadcontent.net/ubuntugis/ppa/ubuntu jammy InRelease\n",
            "Hit:8 http://archive.ubuntu.com/ubuntu jammy InRelease\n",
            "Hit:9 http://archive.ubuntu.com/ubuntu jammy-updates InRelease\n",
            "Hit:10 http://archive.ubuntu.com/ubuntu jammy-backports InRelease\n",
            "Reading package lists... Done\n",
            "W: Skipping acquire of configured file 'main/source/Sources' as repository 'https://r2u.stat.illinois.edu/ubuntu jammy InRelease' does not seem to provide it (sources.list entry misspelt?)\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "chromium-chromedriver is already the newest version (1:85.0.4183.83-0ubuntu2.22.04.1).\n",
            "0 upgraded, 0 newly installed, 0 to remove and 31 not upgraded.\n",
            "Requirement already satisfied: selenium in /usr/local/lib/python3.11/dist-packages (4.29.0)\n",
            "Requirement already satisfied: urllib3<3,>=1.26 in /usr/local/lib/python3.11/dist-packages (from urllib3[socks]<3,>=1.26->selenium) (2.3.0)\n",
            "Requirement already satisfied: trio~=0.17 in /usr/local/lib/python3.11/dist-packages (from selenium) (0.29.0)\n",
            "Requirement already satisfied: trio-websocket~=0.9 in /usr/local/lib/python3.11/dist-packages (from selenium) (0.12.2)\n",
            "Requirement already satisfied: certifi>=2021.10.8 in /usr/local/lib/python3.11/dist-packages (from selenium) (2025.1.31)\n",
            "Requirement already satisfied: typing_extensions~=4.9 in /usr/local/lib/python3.11/dist-packages (from selenium) (4.12.2)\n",
            "Requirement already satisfied: websocket-client~=1.8 in /usr/local/lib/python3.11/dist-packages (from selenium) (1.8.0)\n",
            "Requirement already satisfied: attrs>=23.2.0 in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (25.1.0)\n",
            "Requirement already satisfied: sortedcontainers in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (2.4.0)\n",
            "Requirement already satisfied: idna in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (3.10)\n",
            "Requirement already satisfied: outcome in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (1.3.0.post0)\n",
            "Requirement already satisfied: sniffio>=1.3.0 in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (1.3.1)\n",
            "Requirement already satisfied: wsproto>=0.14 in /usr/local/lib/python3.11/dist-packages (from trio-websocket~=0.9->selenium) (1.2.0)\n",
            "Requirement already satisfied: pysocks!=1.5.7,<2.0,>=1.5.6 in /usr/local/lib/python3.11/dist-packages (from urllib3[socks]<3,>=1.26->selenium) (1.7.1)\n",
            "Requirement already satisfied: h11<1,>=0.9.0 in /usr/local/lib/python3.11/dist-packages (from wsproto>=0.14->trio-websocket~=0.9->selenium) (0.14.0)\n",
            "Requirement already satisfied: webdriver-manager in /usr/local/lib/python3.11/dist-packages (4.0.2)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.11/dist-packages (from webdriver-manager) (2.32.3)\n",
            "Requirement already satisfied: python-dotenv in /usr/local/lib/python3.11/dist-packages (from webdriver-manager) (1.0.1)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.11/dist-packages (from webdriver-manager) (24.2)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests->webdriver-manager) (3.4.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests->webdriver-manager) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests->webdriver-manager) (2.3.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests->webdriver-manager) (2025.1.31)\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "WebDriverException",
          "evalue": "Message: unknown error: Chrome failed to start: exited abnormally.\n  (chrome not reachable)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x5d2dd5fb04e3 <unknown>\n#1 0x5d2dd5cdfc76 <unknown>\n#2 0x5d2dd5d08d78 <unknown>\n#3 0x5d2dd5d05029 <unknown>\n#4 0x5d2dd5d43ccc <unknown>\n#5 0x5d2dd5d4347f <unknown>\n#6 0x5d2dd5d3ade3 <unknown>\n#7 0x5d2dd5d102dd <unknown>\n#8 0x5d2dd5d1134e <unknown>\n#9 0x5d2dd5f703e4 <unknown>\n#10 0x5d2dd5f743d7 <unknown>\n#11 0x5d2dd5f7eb20 <unknown>\n#12 0x5d2dd5f75023 <unknown>\n#13 0x5d2dd5f431aa <unknown>\n#14 0x5d2dd5f996b8 <unknown>\n#15 0x5d2dd5f99847 <unknown>\n#16 0x5d2dd5fa9243 <unknown>\n#17 0x7997baa64ac3 <unknown>\n",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m                        Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-15-9a7ef5c832e9>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     25\u001b[0m \u001b[0;31m# راه‌اندازی ChromeDriver\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     26\u001b[0m \u001b[0mservice\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mService\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mChromeDriverManager\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0minstall\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 27\u001b[0;31m \u001b[0mdriver\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     28\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     29\u001b[0m \u001b[0;31m# باز کردن سایت مورد نظر\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chrome/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     43\u001b[0m         \u001b[0moptions\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0mOptions\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     44\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 45\u001b[0;31m         super().__init__(\n\u001b[0m\u001b[1;32m     46\u001b[0m             \u001b[0mbrowser_name\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mDesiredCapabilities\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCHROME\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"browserName\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     47\u001b[0m             \u001b[0mvendor_prefix\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"goog\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chromium/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, browser_name, vendor_prefix, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     64\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     65\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 66\u001b[0;31m             \u001b[0msuper\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__init__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mexecutor\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     67\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     68\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mquit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, command_executor, keep_alive, file_detector, options, locator_converter, web_element_cls, client_config)\u001b[0m\n\u001b[1;32m    248\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_authenticator_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    249\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_client\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 250\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_session\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    251\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_fedcm\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mFedCM\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    252\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mstart_session\u001b[0;34m(self, capabilities)\u001b[0m\n\u001b[1;32m    340\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    341\u001b[0m         \u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_create_caps\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 342\u001b[0;31m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mCommand\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mNEW_SESSION\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcaps\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    343\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msession_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"sessionId\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    344\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"capabilities\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, driver_command, params)\u001b[0m\n\u001b[1;32m    427\u001b[0m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    428\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 429\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    430\u001b[0m             \u001b[0mresponse\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_unwrap_value\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    431\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/errorhandler.py\u001b[0m in \u001b[0;36mcheck_response\u001b[0;34m(self, response)\u001b[0m\n\u001b[1;32m    230\u001b[0m                 \u001b[0malert_text\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"alert\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"text\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    231\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0malert_text\u001b[0m\u001b[0;34m)\u001b[0m  \u001b[0;31m# type: ignore[call-arg]  # mypy is not smart enough here\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 232\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m: Message: unknown error: Chrome failed to start: exited abnormally.\n  (chrome not reachable)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x5d2dd5fb04e3 <unknown>\n#1 0x5d2dd5cdfc76 <unknown>\n#2 0x5d2dd5d08d78 <unknown>\n#3 0x5d2dd5d05029 <unknown>\n#4 0x5d2dd5d43ccc <unknown>\n#5 0x5d2dd5d4347f <unknown>\n#6 0x5d2dd5d3ade3 <unknown>\n#7 0x5d2dd5d102dd <unknown>\n#8 0x5d2dd5d1134e <unknown>\n#9 0x5d2dd5f703e4 <unknown>\n#10 0x5d2dd5f743d7 <unknown>\n#11 0x5d2dd5f7eb20 <unknown>\n#12 0x5d2dd5f75023 <unknown>\n#13 0x5d2dd5f431aa <unknown>\n#14 0x5d2dd5f996b8 <unknown>\n#15 0x5d2dd5f99847 <unknown>\n#16 0x5d2dd5fa9243 <unknown>\n#17 0x7997baa64ac3 <unknown>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# نصب وابستگی‌ها\n",
        "!apt-get update\n",
        "!apt-get install -y chromium-chromedriver\n",
        "!pip install selenium\n",
        "\n",
        "# تنظیمات Selenium برای استفاده از کروم در Google Colab\n",
        "import sys\n",
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "from webdriver_manager.chrome import ChromeDriverManager\n",
        "\n",
        "# تنظیمات کروم برای استفاده در محیط Google Colab\n",
        "options = Options()\n",
        "options.add_argument('--headless')  # حالت بدون رابط گرافیکی\n",
        "options.add_argument('--no-sandbox')  # برای جلوگیری از مشکلات sandbox\n",
        "options.add_argument('--disable-dev-shm-usage')  # برای بهبود عملکرد در محیط‌های مجازی\n",
        "options.add_argument('--remote-debugging-port=9222')  # برای جلوگیری از خطاهای مربوط به اتصال کروم\n",
        "options.add_argument('--disable-gpu')  # برای رفع مشکلات مربوط به استفاده از GPU\n",
        "\n",
        "# تنظیمات مسیر Chromium به صورت دستی\n",
        "options.binary_location = '/usr/bin/chromium-browser'\n",
        "\n",
        "# راه‌اندازی ChromeDriver با نسخه نصب شده\n",
        "service = Service(\"/usr/lib/chromium-browser/chromedriver\")  # مسیر مشخص به کروم درایور\n",
        "driver = webdriver.Chrome(service=service, options=options)\n",
        "\n",
        "# باز کردن سایت مورد نظر\n",
        "driver.get(\"https://www.futbin.com/\")\n",
        "\n",
        "# ۴. استخراج داده‌ها (منتظر می‌مانیم تا یک عنصر خاص در صفحه بارگذاری شود)\n",
        "from selenium.webdriver.common.by import By\n",
        "from selenium.webdriver.support.ui import WebDriverWait\n",
        "from selenium.webdriver.support import expected_conditions as EC\n",
        "\n",
        "# منتظر می‌مانیم تا عنصر خاصی در صفحه ظاهر شود (در اینجا، لینک‌ها)\n",
        "WebDriverWait(driver, 30).until(\n",
        "    EC.presence_of_element_located((By.CLASS_NAME, 'nav-link'))  # به دنبال لینک‌ها می‌گردیم\n",
        ")\n",
        "\n",
        "# ۵. استخراج لینک‌ها از صفحه\n",
        "links = driver.find_elements(By.CLASS_NAME, 'nav-link')\n",
        "\n",
        "# چاپ تمام لینک‌ها\n",
        "print(\"تمام لینک‌های موجود در منو:\")\n",
        "for link in links:\n",
        "    print(link.text)\n",
        "\n",
        "# ۶. بستن WebDriver پس از اتمام کار\n",
        "driver.quit()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 912
        },
        "id": "YgsNukuAdQWX",
        "outputId": "19b3fab9-2cf0-46bb-8eff-bc7cb58d967a"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hit:1 http://archive.ubuntu.com/ubuntu jammy InRelease\n",
            "Hit:2 http://archive.ubuntu.com/ubuntu jammy-updates InRelease\n",
            "Hit:3 http://archive.ubuntu.com/ubuntu jammy-backports InRelease\n",
            "Hit:4 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64  InRelease\n",
            "Hit:5 https://cloud.r-project.org/bin/linux/ubuntu jammy-cran40/ InRelease\n",
            "Hit:6 https://r2u.stat.illinois.edu/ubuntu jammy InRelease\n",
            "Hit:7 http://security.ubuntu.com/ubuntu jammy-security InRelease\n",
            "Hit:8 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy InRelease\n",
            "Hit:9 https://ppa.launchpadcontent.net/graphics-drivers/ppa/ubuntu jammy InRelease\n",
            "Hit:10 https://ppa.launchpadcontent.net/ubuntugis/ppa/ubuntu jammy InRelease\n",
            "Reading package lists... Done\n",
            "W: Skipping acquire of configured file 'main/source/Sources' as repository 'https://r2u.stat.illinois.edu/ubuntu jammy InRelease' does not seem to provide it (sources.list entry misspelt?)\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "chromium-chromedriver is already the newest version (1:85.0.4183.83-0ubuntu2.22.04.1).\n",
            "0 upgraded, 0 newly installed, 0 to remove and 31 not upgraded.\n",
            "Requirement already satisfied: selenium in /usr/local/lib/python3.11/dist-packages (4.29.0)\n",
            "Requirement already satisfied: urllib3<3,>=1.26 in /usr/local/lib/python3.11/dist-packages (from urllib3[socks]<3,>=1.26->selenium) (2.3.0)\n",
            "Requirement already satisfied: trio~=0.17 in /usr/local/lib/python3.11/dist-packages (from selenium) (0.29.0)\n",
            "Requirement already satisfied: trio-websocket~=0.9 in /usr/local/lib/python3.11/dist-packages (from selenium) (0.12.2)\n",
            "Requirement already satisfied: certifi>=2021.10.8 in /usr/local/lib/python3.11/dist-packages (from selenium) (2025.1.31)\n",
            "Requirement already satisfied: typing_extensions~=4.9 in /usr/local/lib/python3.11/dist-packages (from selenium) (4.12.2)\n",
            "Requirement already satisfied: websocket-client~=1.8 in /usr/local/lib/python3.11/dist-packages (from selenium) (1.8.0)\n",
            "Requirement already satisfied: attrs>=23.2.0 in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (25.1.0)\n",
            "Requirement already satisfied: sortedcontainers in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (2.4.0)\n",
            "Requirement already satisfied: idna in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (3.10)\n",
            "Requirement already satisfied: outcome in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (1.3.0.post0)\n",
            "Requirement already satisfied: sniffio>=1.3.0 in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (1.3.1)\n",
            "Requirement already satisfied: wsproto>=0.14 in /usr/local/lib/python3.11/dist-packages (from trio-websocket~=0.9->selenium) (1.2.0)\n",
            "Requirement already satisfied: pysocks!=1.5.7,<2.0,>=1.5.6 in /usr/local/lib/python3.11/dist-packages (from urllib3[socks]<3,>=1.26->selenium) (1.7.1)\n",
            "Requirement already satisfied: h11<1,>=0.9.0 in /usr/local/lib/python3.11/dist-packages (from wsproto>=0.14->trio-websocket~=0.9->selenium) (0.14.0)\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "WebDriverException",
          "evalue": "Message: Service /usr/lib/chromium-browser/chromedriver unexpectedly exited. Status code was: 1\n",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m                        Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-16-90f56eb8c3f4>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     24\u001b[0m \u001b[0;31m# راه‌اندازی ChromeDriver با نسخه نصب شده\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     25\u001b[0m \u001b[0mservice\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mService\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"/usr/lib/chromium-browser/chromedriver\"\u001b[0m\u001b[0;34m)\u001b[0m  \u001b[0;31m# مسیر مشخص به کروم درایور\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 26\u001b[0;31m \u001b[0mdriver\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     27\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     28\u001b[0m \u001b[0;31m# باز کردن سایت مورد نظر\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chrome/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     43\u001b[0m         \u001b[0moptions\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0mOptions\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     44\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 45\u001b[0;31m         super().__init__(\n\u001b[0m\u001b[1;32m     46\u001b[0m             \u001b[0mbrowser_name\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mDesiredCapabilities\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCHROME\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"browserName\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     47\u001b[0m             \u001b[0mvendor_prefix\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"goog\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chromium/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, browser_name, vendor_prefix, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     53\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     54\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpath\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0menv_path\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0mfinder\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_driver_path\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 55\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     56\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     57\u001b[0m         executor = ChromiumRemoteConnection(\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/common/service.py\u001b[0m in \u001b[0;36mstart\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    111\u001b[0m         \u001b[0mcount\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    112\u001b[0m         \u001b[0;32mwhile\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 113\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0massert_process_still_running\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    114\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mis_connectable\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    115\u001b[0m                 \u001b[0;32mbreak\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/common/service.py\u001b[0m in \u001b[0;36massert_process_still_running\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    124\u001b[0m         \u001b[0mreturn_code\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mprocess\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpoll\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    125\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mreturn_code\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 126\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mWebDriverException\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mf\"Service {self._path} unexpectedly exited. Status code was: {return_code}\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    127\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    128\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mis_connectable\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m->\u001b[0m \u001b[0mbool\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mWebDriverException\u001b[0m: Message: Service /usr/lib/chromium-browser/chromedriver unexpectedly exited. Status code was: 1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from webdriver_manager.chrome import ChromeDriverManager\n",
        "\n",
        "# تنظیمات کروم\n",
        "options = Options()\n",
        "options.add_argument('--headless')  # حالت بدون رابط گرافیکی\n",
        "options.add_argument('--no-sandbox')  # برای جلوگیری از مشکلات sandbox\n",
        "options.add_argument('--disable-dev-shm-usage')  # برای بهبود عملکرد در محیط‌های مجازی\n",
        "options.add_argument('--remote-debugging-port=9222')  # برای جلوگیری از خطاهای مربوط به اتصال کروم\n",
        "options.add_argument('--disable-gpu')  # برای رفع مشکلات مربوط به استفاده از GPU\n",
        "options.binary_location = '/usr/bin/chromium-browser'  # مسیر chromium در colab\n",
        "\n",
        "# نصب خودکار ChromeDriver مناسب برای نسخه کروم\n",
        "service = Service(ChromeDriverManager().install())\n",
        "\n",
        "# راه‌اندازی WebDriver\n",
        "driver = webdriver.Chrome(service=service, options=options)\n",
        "\n",
        "# باز کردن سایت\n",
        "driver.get(\"https://www.futbin.com/\")\n",
        "\n",
        "# بقیه کد برای استخراج داده‌ها\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 686
        },
        "id": "VkUg2GrUdt6f",
        "outputId": "aa2ac162-1016-41c8-a41c-ffe19372c545"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "error",
          "ename": "WebDriverException",
          "evalue": "Message: unknown error: Chrome failed to start: exited abnormally.\n  (chrome not reachable)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x57a84090d4e3 <unknown>\n#1 0x57a84063cc76 <unknown>\n#2 0x57a840665d78 <unknown>\n#3 0x57a840662029 <unknown>\n#4 0x57a8406a0ccc <unknown>\n#5 0x57a8406a047f <unknown>\n#6 0x57a840697de3 <unknown>\n#7 0x57a84066d2dd <unknown>\n#8 0x57a84066e34e <unknown>\n#9 0x57a8408cd3e4 <unknown>\n#10 0x57a8408d13d7 <unknown>\n#11 0x57a8408dbb20 <unknown>\n#12 0x57a8408d2023 <unknown>\n#13 0x57a8408a01aa <unknown>\n#14 0x57a8408f66b8 <unknown>\n#15 0x57a8408f6847 <unknown>\n#16 0x57a840906243 <unknown>\n#17 0x784b4b686ac3 <unknown>\n",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m                        Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-17-1a045b499dd4>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     17\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     18\u001b[0m \u001b[0;31m# راه‌اندازی WebDriver\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 19\u001b[0;31m \u001b[0mdriver\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     20\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     21\u001b[0m \u001b[0;31m# باز کردن سایت\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chrome/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     43\u001b[0m         \u001b[0moptions\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0mOptions\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     44\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 45\u001b[0;31m         super().__init__(\n\u001b[0m\u001b[1;32m     46\u001b[0m             \u001b[0mbrowser_name\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mDesiredCapabilities\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCHROME\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"browserName\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     47\u001b[0m             \u001b[0mvendor_prefix\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"goog\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chromium/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, browser_name, vendor_prefix, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     64\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     65\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 66\u001b[0;31m             \u001b[0msuper\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__init__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mexecutor\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     67\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     68\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mquit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, command_executor, keep_alive, file_detector, options, locator_converter, web_element_cls, client_config)\u001b[0m\n\u001b[1;32m    248\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_authenticator_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    249\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_client\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 250\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_session\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    251\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_fedcm\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mFedCM\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    252\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mstart_session\u001b[0;34m(self, capabilities)\u001b[0m\n\u001b[1;32m    340\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    341\u001b[0m         \u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_create_caps\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 342\u001b[0;31m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mCommand\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mNEW_SESSION\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcaps\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    343\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msession_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"sessionId\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    344\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"capabilities\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, driver_command, params)\u001b[0m\n\u001b[1;32m    427\u001b[0m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    428\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 429\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    430\u001b[0m             \u001b[0mresponse\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_unwrap_value\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    431\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/errorhandler.py\u001b[0m in \u001b[0;36mcheck_response\u001b[0;34m(self, response)\u001b[0m\n\u001b[1;32m    230\u001b[0m                 \u001b[0malert_text\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"alert\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"text\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    231\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0malert_text\u001b[0m\u001b[0;34m)\u001b[0m  \u001b[0;31m# type: ignore[call-arg]  # mypy is not smart enough here\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 232\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m: Message: unknown error: Chrome failed to start: exited abnormally.\n  (chrome not reachable)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x57a84090d4e3 <unknown>\n#1 0x57a84063cc76 <unknown>\n#2 0x57a840665d78 <unknown>\n#3 0x57a840662029 <unknown>\n#4 0x57a8406a0ccc <unknown>\n#5 0x57a8406a047f <unknown>\n#6 0x57a840697de3 <unknown>\n#7 0x57a84066d2dd <unknown>\n#8 0x57a84066e34e <unknown>\n#9 0x57a8408cd3e4 <unknown>\n#10 0x57a8408d13d7 <unknown>\n#11 0x57a8408dbb20 <unknown>\n#12 0x57a8408d2023 <unknown>\n#13 0x57a8408a01aa <unknown>\n#14 0x57a8408f66b8 <unknown>\n#15 0x57a8408f6847 <unknown>\n#16 0x57a840906243 <unknown>\n#17 0x784b4b686ac3 <unknown>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from webdriver_manager.chrome import ChromeDriverManager\n",
        "\n",
        "# تنظیمات کروم\n",
        "options = Options()\n",
        "options.add_argument('--headless')  # حالت بدون رابط گرافیکی\n",
        "options.add_argument('--no-sandbox')  # برای جلوگیری از مشکلات sandbox\n",
        "options.add_argument('--disable-dev-shm-usage')  # برای بهبود عملکرد در محیط‌های مجازی\n",
        "options.add_argument('--remote-debugging-port=9222')  # برای جلوگیری از خطاهای مربوط به اتصال کروم\n",
        "options.add_argument('--disable-gpu')  # برای رفع مشکلات مربوط به استفاده از GPU\n",
        "options.binary_location = '/usr/bin/chromium-browser'  # مسیر chromium در colab\n",
        "\n",
        "# نصب خودکار ChromeDriver مناسب برای نسخه کروم\n",
        "service = Service(ChromeDriverManager().install())\n",
        "\n",
        "# راه‌اندازی WebDriver\n",
        "driver = webdriver.Chrome(service=service, options=options)\n",
        "\n",
        "# باز کردن سایت\n",
        "driver.get(\"https://www.futbin.com/\")\n",
        "\n",
        "# بقیه کد برای استخراج داده‌ها\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 686
        },
        "id": "ZNiRRjemd2bK",
        "outputId": "3b068315-d32b-4013-f695-0ccc1fdd9ee6"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "error",
          "ename": "WebDriverException",
          "evalue": "Message: unknown error: Chrome failed to start: exited abnormally.\n  (chrome not reachable)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x585ffcb314e3 <unknown>\n#1 0x585ffc860c76 <unknown>\n#2 0x585ffc889d78 <unknown>\n#3 0x585ffc886029 <unknown>\n#4 0x585ffc8c4ccc <unknown>\n#5 0x585ffc8c447f <unknown>\n#6 0x585ffc8bbde3 <unknown>\n#7 0x585ffc8912dd <unknown>\n#8 0x585ffc89234e <unknown>\n#9 0x585ffcaf13e4 <unknown>\n#10 0x585ffcaf53d7 <unknown>\n#11 0x585ffcaffb20 <unknown>\n#12 0x585ffcaf6023 <unknown>\n#13 0x585ffcac41aa <unknown>\n#14 0x585ffcb1a6b8 <unknown>\n#15 0x585ffcb1a847 <unknown>\n#16 0x585ffcb2a243 <unknown>\n#17 0x794ddfea5ac3 <unknown>\n",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m                        Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-18-1a045b499dd4>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     17\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     18\u001b[0m \u001b[0;31m# راه‌اندازی WebDriver\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 19\u001b[0;31m \u001b[0mdriver\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     20\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     21\u001b[0m \u001b[0;31m# باز کردن سایت\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chrome/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     43\u001b[0m         \u001b[0moptions\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0mOptions\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     44\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 45\u001b[0;31m         super().__init__(\n\u001b[0m\u001b[1;32m     46\u001b[0m             \u001b[0mbrowser_name\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mDesiredCapabilities\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCHROME\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"browserName\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     47\u001b[0m             \u001b[0mvendor_prefix\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"goog\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chromium/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, browser_name, vendor_prefix, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     64\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     65\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 66\u001b[0;31m             \u001b[0msuper\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__init__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mexecutor\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     67\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     68\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mquit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, command_executor, keep_alive, file_detector, options, locator_converter, web_element_cls, client_config)\u001b[0m\n\u001b[1;32m    248\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_authenticator_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    249\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_client\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 250\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_session\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    251\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_fedcm\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mFedCM\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    252\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mstart_session\u001b[0;34m(self, capabilities)\u001b[0m\n\u001b[1;32m    340\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    341\u001b[0m         \u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_create_caps\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 342\u001b[0;31m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mCommand\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mNEW_SESSION\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcaps\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    343\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msession_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"sessionId\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    344\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"capabilities\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, driver_command, params)\u001b[0m\n\u001b[1;32m    427\u001b[0m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    428\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 429\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    430\u001b[0m             \u001b[0mresponse\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_unwrap_value\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    431\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/errorhandler.py\u001b[0m in \u001b[0;36mcheck_response\u001b[0;34m(self, response)\u001b[0m\n\u001b[1;32m    230\u001b[0m                 \u001b[0malert_text\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"alert\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"text\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    231\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0malert_text\u001b[0m\u001b[0;34m)\u001b[0m  \u001b[0;31m# type: ignore[call-arg]  # mypy is not smart enough here\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 232\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m: Message: unknown error: Chrome failed to start: exited abnormally.\n  (chrome not reachable)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x585ffcb314e3 <unknown>\n#1 0x585ffc860c76 <unknown>\n#2 0x585ffc889d78 <unknown>\n#3 0x585ffc886029 <unknown>\n#4 0x585ffc8c4ccc <unknown>\n#5 0x585ffc8c447f <unknown>\n#6 0x585ffc8bbde3 <unknown>\n#7 0x585ffc8912dd <unknown>\n#8 0x585ffc89234e <unknown>\n#9 0x585ffcaf13e4 <unknown>\n#10 0x585ffcaf53d7 <unknown>\n#11 0x585ffcaffb20 <unknown>\n#12 0x585ffcaf6023 <unknown>\n#13 0x585ffcac41aa <unknown>\n#14 0x585ffcb1a6b8 <unknown>\n#15 0x585ffcb1a847 <unknown>\n#16 0x585ffcb2a243 <unknown>\n#17 0x794ddfea5ac3 <unknown>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from webdriver_manager.chrome import ChromeDriverManager\n",
        "\n",
        "# تنظیمات کروم\n",
        "options = Options()\n",
        "options.add_argument('--headless')  # حالت بدون رابط گرافیکی\n",
        "options.add_argument('--no-sandbox')  # برای جلوگیری از مشکلات sandbox\n",
        "options.add_argument('--disable-dev-shm-usage')  # برای بهبود عملکرد در محیط‌های مجازی\n",
        "options.add_argument('--remote-debugging-port=9222')  # برای جلوگیری از خطاهای مربوط به اتصال کروم\n",
        "options.add_argument('--disable-gpu')  # برای رفع مشکلات مربوط به استفاده از GPU\n",
        "options.binary_location = '/usr/bin/chromium-browser'  # مسیر chromium در colab\n",
        "\n",
        "# نصب خودکار ChromeDriver مناسب برای نسخه کروم\n",
        "service = Service(ChromeDriverManager().install())\n",
        "\n",
        "# راه‌اندازی WebDriver\n",
        "driver = webdriver.Chrome(service=service, options=options)\n",
        "\n",
        "# باز کردن سایت\n",
        "driver.get(\"https://www.futbin.com/\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 686
        },
        "id": "xrznRCXYeBwq",
        "outputId": "6437baf6-30f6-4b20-92a1-8496e1a3e951"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "error",
          "ename": "WebDriverException",
          "evalue": "Message: unknown error: Chrome failed to start: exited abnormally.\n  (chrome not reachable)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x576d670de4e3 <unknown>\n#1 0x576d66e0dc76 <unknown>\n#2 0x576d66e36d78 <unknown>\n#3 0x576d66e33029 <unknown>\n#4 0x576d66e71ccc <unknown>\n#5 0x576d66e7147f <unknown>\n#6 0x576d66e68de3 <unknown>\n#7 0x576d66e3e2dd <unknown>\n#8 0x576d66e3f34e <unknown>\n#9 0x576d6709e3e4 <unknown>\n#10 0x576d670a23d7 <unknown>\n#11 0x576d670acb20 <unknown>\n#12 0x576d670a3023 <unknown>\n#13 0x576d670711aa <unknown>\n#14 0x576d670c76b8 <unknown>\n#15 0x576d670c7847 <unknown>\n#16 0x576d670d7243 <unknown>\n#17 0x7cc11d37bac3 <unknown>\n",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m                        Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-19-08f2115f0eef>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     17\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     18\u001b[0m \u001b[0;31m# راه‌اندازی WebDriver\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 19\u001b[0;31m \u001b[0mdriver\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     20\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     21\u001b[0m \u001b[0;31m# باز کردن سایت\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chrome/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     43\u001b[0m         \u001b[0moptions\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0mOptions\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     44\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 45\u001b[0;31m         super().__init__(\n\u001b[0m\u001b[1;32m     46\u001b[0m             \u001b[0mbrowser_name\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mDesiredCapabilities\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCHROME\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"browserName\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     47\u001b[0m             \u001b[0mvendor_prefix\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"goog\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chromium/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, browser_name, vendor_prefix, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     64\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     65\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 66\u001b[0;31m             \u001b[0msuper\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__init__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mexecutor\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     67\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     68\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mquit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, command_executor, keep_alive, file_detector, options, locator_converter, web_element_cls, client_config)\u001b[0m\n\u001b[1;32m    248\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_authenticator_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    249\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_client\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 250\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_session\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    251\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_fedcm\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mFedCM\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    252\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mstart_session\u001b[0;34m(self, capabilities)\u001b[0m\n\u001b[1;32m    340\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    341\u001b[0m         \u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_create_caps\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 342\u001b[0;31m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mCommand\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mNEW_SESSION\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcaps\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    343\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msession_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"sessionId\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    344\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"capabilities\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, driver_command, params)\u001b[0m\n\u001b[1;32m    427\u001b[0m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    428\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 429\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    430\u001b[0m             \u001b[0mresponse\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_unwrap_value\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    431\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/errorhandler.py\u001b[0m in \u001b[0;36mcheck_response\u001b[0;34m(self, response)\u001b[0m\n\u001b[1;32m    230\u001b[0m                 \u001b[0malert_text\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"alert\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"text\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    231\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0malert_text\u001b[0m\u001b[0;34m)\u001b[0m  \u001b[0;31m# type: ignore[call-arg]  # mypy is not smart enough here\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 232\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m: Message: unknown error: Chrome failed to start: exited abnormally.\n  (chrome not reachable)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x576d670de4e3 <unknown>\n#1 0x576d66e0dc76 <unknown>\n#2 0x576d66e36d78 <unknown>\n#3 0x576d66e33029 <unknown>\n#4 0x576d66e71ccc <unknown>\n#5 0x576d66e7147f <unknown>\n#6 0x576d66e68de3 <unknown>\n#7 0x576d66e3e2dd <unknown>\n#8 0x576d66e3f34e <unknown>\n#9 0x576d6709e3e4 <unknown>\n#10 0x576d670a23d7 <unknown>\n#11 0x576d670acb20 <unknown>\n#12 0x576d670a3023 <unknown>\n#13 0x576d670711aa <unknown>\n#14 0x576d670c76b8 <unknown>\n#15 0x576d670c7847 <unknown>\n#16 0x576d670d7243 <unknown>\n#17 0x7cc11d37bac3 <unknown>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from webdriver_manager.chrome import ChromeDriverManager\n",
        "\n",
        "# تنظیمات کروم\n",
        "options = Options()\n",
        "options.add_argument('--headless')  # حالت بدون رابط گرافیکی\n",
        "options.add_argument('--no-sandbox')  # برای جلوگیری از مشکلات sandbox\n",
        "options.add_argument('--disable-dev-shm-usage')  # برای بهبود عملکرد در محیط‌های مجازی\n",
        "options.add_argument('--remote-debugging-port=9222')  # برای جلوگیری از خطاهای مربوط به اتصال کروم\n",
        "options.add_argument('--disable-gpu')  # برای رفع مشکلات مربوط به استفاده از GPU\n",
        "options.binary_location = '/usr/bin/chromium-browser'  # مسیر chromium در colab\n",
        "\n",
        "# نصب خودکار ChromeDriver مناسب برای نسخه کروم\n",
        "service = Service(ChromeDriverManager().install())\n",
        "\n",
        "# راه‌اندازی WebDriver\n",
        "driver = webdriver.Chrome(service=service, options=options)\n",
        "\n",
        "# باز کردن سایت\n",
        "driver.get(\"https://www.futbin.com/\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 686
        },
        "id": "sR_nIRoZeL5e",
        "outputId": "bf427751-fad7-454a-c304-4c6ff20360e1"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "error",
          "ename": "WebDriverException",
          "evalue": "Message: unknown error: Chrome failed to start: exited abnormally.\n  (chrome not reachable)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x5c0e8eb734e3 <unknown>\n#1 0x5c0e8e8a2c76 <unknown>\n#2 0x5c0e8e8cbd78 <unknown>\n#3 0x5c0e8e8c8029 <unknown>\n#4 0x5c0e8e906ccc <unknown>\n#5 0x5c0e8e90647f <unknown>\n#6 0x5c0e8e8fdde3 <unknown>\n#7 0x5c0e8e8d32dd <unknown>\n#8 0x5c0e8e8d434e <unknown>\n#9 0x5c0e8eb333e4 <unknown>\n#10 0x5c0e8eb373d7 <unknown>\n#11 0x5c0e8eb41b20 <unknown>\n#12 0x5c0e8eb38023 <unknown>\n#13 0x5c0e8eb061aa <unknown>\n#14 0x5c0e8eb5c6b8 <unknown>\n#15 0x5c0e8eb5c847 <unknown>\n#16 0x5c0e8eb6c243 <unknown>\n#17 0x7fd68d2dbac3 <unknown>\n",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m                        Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-20-08f2115f0eef>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     17\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     18\u001b[0m \u001b[0;31m# راه‌اندازی WebDriver\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 19\u001b[0;31m \u001b[0mdriver\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     20\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     21\u001b[0m \u001b[0;31m# باز کردن سایت\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chrome/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     43\u001b[0m         \u001b[0moptions\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0mOptions\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     44\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 45\u001b[0;31m         super().__init__(\n\u001b[0m\u001b[1;32m     46\u001b[0m             \u001b[0mbrowser_name\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mDesiredCapabilities\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCHROME\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"browserName\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     47\u001b[0m             \u001b[0mvendor_prefix\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"goog\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chromium/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, browser_name, vendor_prefix, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     64\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     65\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 66\u001b[0;31m             \u001b[0msuper\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__init__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mexecutor\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     67\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     68\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mquit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, command_executor, keep_alive, file_detector, options, locator_converter, web_element_cls, client_config)\u001b[0m\n\u001b[1;32m    248\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_authenticator_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    249\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_client\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 250\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_session\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    251\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_fedcm\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mFedCM\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    252\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mstart_session\u001b[0;34m(self, capabilities)\u001b[0m\n\u001b[1;32m    340\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    341\u001b[0m         \u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_create_caps\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 342\u001b[0;31m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mCommand\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mNEW_SESSION\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcaps\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    343\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msession_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"sessionId\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    344\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"capabilities\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, driver_command, params)\u001b[0m\n\u001b[1;32m    427\u001b[0m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    428\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 429\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    430\u001b[0m             \u001b[0mresponse\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_unwrap_value\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    431\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/errorhandler.py\u001b[0m in \u001b[0;36mcheck_response\u001b[0;34m(self, response)\u001b[0m\n\u001b[1;32m    230\u001b[0m                 \u001b[0malert_text\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"alert\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"text\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    231\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0malert_text\u001b[0m\u001b[0;34m)\u001b[0m  \u001b[0;31m# type: ignore[call-arg]  # mypy is not smart enough here\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 232\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m: Message: unknown error: Chrome failed to start: exited abnormally.\n  (chrome not reachable)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x5c0e8eb734e3 <unknown>\n#1 0x5c0e8e8a2c76 <unknown>\n#2 0x5c0e8e8cbd78 <unknown>\n#3 0x5c0e8e8c8029 <unknown>\n#4 0x5c0e8e906ccc <unknown>\n#5 0x5c0e8e90647f <unknown>\n#6 0x5c0e8e8fdde3 <unknown>\n#7 0x5c0e8e8d32dd <unknown>\n#8 0x5c0e8e8d434e <unknown>\n#9 0x5c0e8eb333e4 <unknown>\n#10 0x5c0e8eb373d7 <unknown>\n#11 0x5c0e8eb41b20 <unknown>\n#12 0x5c0e8eb38023 <unknown>\n#13 0x5c0e8eb061aa <unknown>\n#14 0x5c0e8eb5c6b8 <unknown>\n#15 0x5c0e8eb5c847 <unknown>\n#16 0x5c0e8eb6c243 <unknown>\n#17 0x7fd68d2dbac3 <unknown>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from webdriver_manager.chrome import ChromeDriverManager\n",
        "\n",
        "# تنظیمات کروم\n",
        "options = Options()\n",
        "options.add_argument('--headless')  # حالت بدون رابط گرافیکی\n",
        "options.add_argument('--no-sandbox')  # برای جلوگیری از مشکلات sandbox\n",
        "options.add_argument('--disable-dev-shm-usage')  # برای بهبود عملکرد در محیط‌های مجازی\n",
        "options.add_argument('--remote-debugging-port=9222')  # برای جلوگیری از خطاهای مربوط به اتصال کروم\n",
        "options.add_argument('--disable-gpu')  # برای رفع مشکلات مربوط به استفاده از GPU\n",
        "options.add_argument('--disable-software-rasterizer')  # برای غیرفعال کردن رستر ساز\n",
        "options.add_argument('start-maximized')  # باز کردن کروم در حالت حداکثر\n",
        "\n",
        "# مسیر کروم درایور\n",
        "options.binary_location = '/usr/bin/chromium-browser'\n",
        "\n",
        "# نصب خودکار ChromeDriver مناسب برای نسخه کروم\n",
        "service = Service(ChromeDriverManager().install())\n",
        "\n",
        "# راه‌اندازی WebDriver\n",
        "driver = webdriver.Chrome(service=service, options=options)\n",
        "\n",
        "# باز کردن سایت\n",
        "driver.get(\"https://www.futbin.com/\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 686
        },
        "id": "uNAPZ0WgeSWB",
        "outputId": "2625dfe7-8997-4602-f492-2f4b34b3f7f0"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "error",
          "ename": "WebDriverException",
          "evalue": "Message: unknown error: Chrome failed to start: exited abnormally.\n  (chrome not reachable)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x58c9aebfa4e3 <unknown>\n#1 0x58c9ae929c76 <unknown>\n#2 0x58c9ae952d78 <unknown>\n#3 0x58c9ae94f029 <unknown>\n#4 0x58c9ae98dccc <unknown>\n#5 0x58c9ae98d47f <unknown>\n#6 0x58c9ae984de3 <unknown>\n#7 0x58c9ae95a2dd <unknown>\n#8 0x58c9ae95b34e <unknown>\n#9 0x58c9aebba3e4 <unknown>\n#10 0x58c9aebbe3d7 <unknown>\n#11 0x58c9aebc8b20 <unknown>\n#12 0x58c9aebbf023 <unknown>\n#13 0x58c9aeb8d1aa <unknown>\n#14 0x58c9aebe36b8 <unknown>\n#15 0x58c9aebe3847 <unknown>\n#16 0x58c9aebf3243 <unknown>\n#17 0x7b62ea042ac3 <unknown>\n",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m                        Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-21-96551b362e7d>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     21\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     22\u001b[0m \u001b[0;31m# راه‌اندازی WebDriver\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 23\u001b[0;31m \u001b[0mdriver\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     24\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     25\u001b[0m \u001b[0;31m# باز کردن سایت\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chrome/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     43\u001b[0m         \u001b[0moptions\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0mOptions\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     44\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 45\u001b[0;31m         super().__init__(\n\u001b[0m\u001b[1;32m     46\u001b[0m             \u001b[0mbrowser_name\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mDesiredCapabilities\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCHROME\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"browserName\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     47\u001b[0m             \u001b[0mvendor_prefix\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"goog\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chromium/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, browser_name, vendor_prefix, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     64\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     65\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 66\u001b[0;31m             \u001b[0msuper\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__init__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mexecutor\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     67\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     68\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mquit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, command_executor, keep_alive, file_detector, options, locator_converter, web_element_cls, client_config)\u001b[0m\n\u001b[1;32m    248\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_authenticator_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    249\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_client\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 250\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_session\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    251\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_fedcm\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mFedCM\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    252\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mstart_session\u001b[0;34m(self, capabilities)\u001b[0m\n\u001b[1;32m    340\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    341\u001b[0m         \u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_create_caps\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 342\u001b[0;31m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mCommand\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mNEW_SESSION\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcaps\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    343\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msession_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"sessionId\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    344\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"capabilities\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, driver_command, params)\u001b[0m\n\u001b[1;32m    427\u001b[0m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    428\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 429\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    430\u001b[0m             \u001b[0mresponse\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_unwrap_value\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    431\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/errorhandler.py\u001b[0m in \u001b[0;36mcheck_response\u001b[0;34m(self, response)\u001b[0m\n\u001b[1;32m    230\u001b[0m                 \u001b[0malert_text\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"alert\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"text\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    231\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0malert_text\u001b[0m\u001b[0;34m)\u001b[0m  \u001b[0;31m# type: ignore[call-arg]  # mypy is not smart enough here\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 232\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m: Message: unknown error: Chrome failed to start: exited abnormally.\n  (chrome not reachable)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x58c9aebfa4e3 <unknown>\n#1 0x58c9ae929c76 <unknown>\n#2 0x58c9ae952d78 <unknown>\n#3 0x58c9ae94f029 <unknown>\n#4 0x58c9ae98dccc <unknown>\n#5 0x58c9ae98d47f <unknown>\n#6 0x58c9ae984de3 <unknown>\n#7 0x58c9ae95a2dd <unknown>\n#8 0x58c9ae95b34e <unknown>\n#9 0x58c9aebba3e4 <unknown>\n#10 0x58c9aebbe3d7 <unknown>\n#11 0x58c9aebc8b20 <unknown>\n#12 0x58c9aebbf023 <unknown>\n#13 0x58c9aeb8d1aa <unknown>\n#14 0x58c9aebe36b8 <unknown>\n#15 0x58c9aebe3847 <unknown>\n#16 0x58c9aebf3243 <unknown>\n#17 0x7b62ea042ac3 <unknown>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from webdriver_manager.chrome import ChromeDriverManager\n",
        "\n",
        "# تنظیمات کروم\n",
        "options = Options()\n",
        "options.add_argument('--headless')  # حالت بدون رابط گرافیکی\n",
        "options.add_argument('--no-sandbox')  # برای جلوگیری از مشکلات sandbox\n",
        "options.add_argument('--disable-dev-shm-usage')  # برای بهبود عملکرد در محیط‌های مجازی\n",
        "options.add_argument('--remote-debugging-port=9222')  # برای جلوگیری از خطاهای مربوط به اتصال کروم\n",
        "options.add_argument('--disable-gpu')  # برای رفع مشکلات مربوط به استفاده از GPU\n",
        "options.add_argument('--disable-software-rasterizer')  # برای غیرفعال کردن رستر ساز\n",
        "options.add_argument('start-maximized')  # باز کردن کروم در حالت حداکثر\n",
        "\n",
        "# مسیر کروم درایور\n",
        "options.binary_location = '/usr/bin/chromium-browser'\n",
        "\n",
        "# نصب خودکار ChromeDriver مناسب برای نسخه کروم\n",
        "service = Service(ChromeDriverManager().install())\n",
        "\n",
        "# راه‌اندازی WebDriver\n",
        "driver = webdriver.Chrome(service=service, options=options)\n",
        "\n",
        "# باز کردن سایت\n",
        "driver.get(\"https://www.futbin.com/\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 686
        },
        "id": "pLh_5g4NeYv5",
        "outputId": "20d26ef1-d2a9-4f15-bbbd-1869c66e5388"
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "error",
          "ename": "WebDriverException",
          "evalue": "Message: unknown error: Chrome failed to start: exited abnormally.\n  (chrome not reachable)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x5ce80afd94e3 <unknown>\n#1 0x5ce80ad08c76 <unknown>\n#2 0x5ce80ad31d78 <unknown>\n#3 0x5ce80ad2e029 <unknown>\n#4 0x5ce80ad6cccc <unknown>\n#5 0x5ce80ad6c47f <unknown>\n#6 0x5ce80ad63de3 <unknown>\n#7 0x5ce80ad392dd <unknown>\n#8 0x5ce80ad3a34e <unknown>\n#9 0x5ce80af993e4 <unknown>\n#10 0x5ce80af9d3d7 <unknown>\n#11 0x5ce80afa7b20 <unknown>\n#12 0x5ce80af9e023 <unknown>\n#13 0x5ce80af6c1aa <unknown>\n#14 0x5ce80afc26b8 <unknown>\n#15 0x5ce80afc2847 <unknown>\n#16 0x5ce80afd2243 <unknown>\n#17 0x7cf28423eac3 <unknown>\n",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m                        Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-22-96551b362e7d>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     21\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     22\u001b[0m \u001b[0;31m# راه‌اندازی WebDriver\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 23\u001b[0;31m \u001b[0mdriver\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     24\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     25\u001b[0m \u001b[0;31m# باز کردن سایت\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chrome/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     43\u001b[0m         \u001b[0moptions\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0mOptions\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     44\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 45\u001b[0;31m         super().__init__(\n\u001b[0m\u001b[1;32m     46\u001b[0m             \u001b[0mbrowser_name\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mDesiredCapabilities\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCHROME\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"browserName\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     47\u001b[0m             \u001b[0mvendor_prefix\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"goog\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chromium/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, browser_name, vendor_prefix, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     64\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     65\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 66\u001b[0;31m             \u001b[0msuper\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__init__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mexecutor\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     67\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     68\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mquit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, command_executor, keep_alive, file_detector, options, locator_converter, web_element_cls, client_config)\u001b[0m\n\u001b[1;32m    248\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_authenticator_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    249\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_client\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 250\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_session\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    251\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_fedcm\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mFedCM\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    252\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mstart_session\u001b[0;34m(self, capabilities)\u001b[0m\n\u001b[1;32m    340\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    341\u001b[0m         \u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_create_caps\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 342\u001b[0;31m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mCommand\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mNEW_SESSION\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcaps\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    343\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msession_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"sessionId\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    344\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"capabilities\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, driver_command, params)\u001b[0m\n\u001b[1;32m    427\u001b[0m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    428\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 429\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    430\u001b[0m             \u001b[0mresponse\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_unwrap_value\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    431\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/errorhandler.py\u001b[0m in \u001b[0;36mcheck_response\u001b[0;34m(self, response)\u001b[0m\n\u001b[1;32m    230\u001b[0m                 \u001b[0malert_text\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"alert\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"text\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    231\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0malert_text\u001b[0m\u001b[0;34m)\u001b[0m  \u001b[0;31m# type: ignore[call-arg]  # mypy is not smart enough here\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 232\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m: Message: unknown error: Chrome failed to start: exited abnormally.\n  (chrome not reachable)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x5ce80afd94e3 <unknown>\n#1 0x5ce80ad08c76 <unknown>\n#2 0x5ce80ad31d78 <unknown>\n#3 0x5ce80ad2e029 <unknown>\n#4 0x5ce80ad6cccc <unknown>\n#5 0x5ce80ad6c47f <unknown>\n#6 0x5ce80ad63de3 <unknown>\n#7 0x5ce80ad392dd <unknown>\n#8 0x5ce80ad3a34e <unknown>\n#9 0x5ce80af993e4 <unknown>\n#10 0x5ce80af9d3d7 <unknown>\n#11 0x5ce80afa7b20 <unknown>\n#12 0x5ce80af9e023 <unknown>\n#13 0x5ce80af6c1aa <unknown>\n#14 0x5ce80afc26b8 <unknown>\n#15 0x5ce80afc2847 <unknown>\n#16 0x5ce80afd2243 <unknown>\n#17 0x7cf28423eac3 <unknown>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from webdriver_manager.chrome import ChromeDriverManager\n",
        "\n",
        "# تنظیمات کروم\n",
        "options = Options()\n",
        "options.add_argument('--headless')  # حالت بدون رابط گرافیکی\n",
        "options.add_argument('--no-sandbox')  # برای جلوگیری از مشکلات sandbox\n",
        "options.add_argument('--disable-dev-shm-usage')  # برای بهبود عملکرد در محیط‌های مجازی\n",
        "options.add_argument('--remote-debugging-port=9222')  # برای جلوگیری از خطاهای مربوط به اتصال کروم\n",
        "options.add_argument('--disable-gpu')  # برای رفع مشکلات مربوط به استفاده از GPU\n",
        "options.add_argument('--disable-software-rasterizer')  # برای غیرفعال کردن رستر ساز\n",
        "options.add_argument('--start-maximized')  # باز کردن کروم در حالت حداکثر\n",
        "options.add_argument('--disable-extensions')  # غیرفعال کردن اکستنشن‌ها\n",
        "\n",
        "# مسیر کروم درایور\n",
        "options.binary_location = '/usr/bin/chromium-browser'\n",
        "\n",
        "# نصب خودکار ChromeDriver مناسب برای نسخه کروم\n",
        "service = Service(ChromeDriverManager().install())\n",
        "\n",
        "# راه‌اندازی WebDriver\n",
        "driver = webdriver.Chrome(service=service, options=options)\n",
        "\n",
        "# باز کردن سایت\n",
        "driver.get(\"https://www.futbin.com/\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 686
        },
        "id": "hX7PlKihefjv",
        "outputId": "95f5a96c-146b-4959-d5ce-501c6ab3f5af"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "error",
          "ename": "WebDriverException",
          "evalue": "Message: unknown error: Chrome failed to start: exited abnormally.\n  (chrome not reachable)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x56cf2fad54e3 <unknown>\n#1 0x56cf2f804c76 <unknown>\n#2 0x56cf2f82dd78 <unknown>\n#3 0x56cf2f82a029 <unknown>\n#4 0x56cf2f868ccc <unknown>\n#5 0x56cf2f86847f <unknown>\n#6 0x56cf2f85fde3 <unknown>\n#7 0x56cf2f8352dd <unknown>\n#8 0x56cf2f83634e <unknown>\n#9 0x56cf2fa953e4 <unknown>\n#10 0x56cf2fa993d7 <unknown>\n#11 0x56cf2faa3b20 <unknown>\n#12 0x56cf2fa9a023 <unknown>\n#13 0x56cf2fa681aa <unknown>\n#14 0x56cf2fabe6b8 <unknown>\n#15 0x56cf2fabe847 <unknown>\n#16 0x56cf2face243 <unknown>\n#17 0x7c5d708b4ac3 <unknown>\n",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m                        Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-23-85784bd9956b>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     22\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     23\u001b[0m \u001b[0;31m# راه‌اندازی WebDriver\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 24\u001b[0;31m \u001b[0mdriver\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     25\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     26\u001b[0m \u001b[0;31m# باز کردن سایت\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chrome/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     43\u001b[0m         \u001b[0moptions\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0mOptions\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     44\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 45\u001b[0;31m         super().__init__(\n\u001b[0m\u001b[1;32m     46\u001b[0m             \u001b[0mbrowser_name\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mDesiredCapabilities\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCHROME\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"browserName\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     47\u001b[0m             \u001b[0mvendor_prefix\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"goog\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chromium/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, browser_name, vendor_prefix, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     64\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     65\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 66\u001b[0;31m             \u001b[0msuper\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__init__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mexecutor\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     67\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     68\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mquit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, command_executor, keep_alive, file_detector, options, locator_converter, web_element_cls, client_config)\u001b[0m\n\u001b[1;32m    248\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_authenticator_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    249\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_client\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 250\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_session\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    251\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_fedcm\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mFedCM\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    252\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mstart_session\u001b[0;34m(self, capabilities)\u001b[0m\n\u001b[1;32m    340\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    341\u001b[0m         \u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_create_caps\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 342\u001b[0;31m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mCommand\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mNEW_SESSION\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcaps\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    343\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msession_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"sessionId\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    344\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"capabilities\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, driver_command, params)\u001b[0m\n\u001b[1;32m    427\u001b[0m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    428\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 429\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    430\u001b[0m             \u001b[0mresponse\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_unwrap_value\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    431\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/errorhandler.py\u001b[0m in \u001b[0;36mcheck_response\u001b[0;34m(self, response)\u001b[0m\n\u001b[1;32m    230\u001b[0m                 \u001b[0malert_text\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"alert\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"text\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    231\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0malert_text\u001b[0m\u001b[0;34m)\u001b[0m  \u001b[0;31m# type: ignore[call-arg]  # mypy is not smart enough here\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 232\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m: Message: unknown error: Chrome failed to start: exited abnormally.\n  (chrome not reachable)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x56cf2fad54e3 <unknown>\n#1 0x56cf2f804c76 <unknown>\n#2 0x56cf2f82dd78 <unknown>\n#3 0x56cf2f82a029 <unknown>\n#4 0x56cf2f868ccc <unknown>\n#5 0x56cf2f86847f <unknown>\n#6 0x56cf2f85fde3 <unknown>\n#7 0x56cf2f8352dd <unknown>\n#8 0x56cf2f83634e <unknown>\n#9 0x56cf2fa953e4 <unknown>\n#10 0x56cf2fa993d7 <unknown>\n#11 0x56cf2faa3b20 <unknown>\n#12 0x56cf2fa9a023 <unknown>\n#13 0x56cf2fa681aa <unknown>\n#14 0x56cf2fabe6b8 <unknown>\n#15 0x56cf2fabe847 <unknown>\n#16 0x56cf2face243 <unknown>\n#17 0x7c5d708b4ac3 <unknown>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "chromium-browser --version\n",
        "chromedriver --version\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 159
        },
        "id": "Yv6eu0MeekxF",
        "outputId": "cb4a771f-87f2-4884-906c-b7e6303f95e1"
      },
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "name 'chromium' is not defined",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-24-4acb6a48178b>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mchromium\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0mbrowser\u001b[0m \u001b[0;34m-\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0mversion\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0mchromedriver\u001b[0m \u001b[0;34m-\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0mversion\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mNameError\u001b[0m: name 'chromium' is not defined"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!apt-get update # بروزرسانی پکیج‌ها\n",
        "!apt-get install -y chromium-chromedriver # نصب کروم و کروم درایور\n",
        "!pip install -q selenium # نصب Selenium\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IgcLr9wJevLT",
        "outputId": "aa540c64-b500-480c-f10a-80012ad9111c"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\r0% [Working]\r            \rHit:1 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64  InRelease\n",
            "\r0% [Waiting for headers] [Connecting to security.ubuntu.com (91.189.91.83)] [Connected to cloud.r-pr\r                                                                                                    \rHit:2 http://archive.ubuntu.com/ubuntu jammy InRelease\n",
            "Hit:3 http://archive.ubuntu.com/ubuntu jammy-updates InRelease\n",
            "Hit:4 http://archive.ubuntu.com/ubuntu jammy-backports InRelease\n",
            "Hit:5 https://r2u.stat.illinois.edu/ubuntu jammy InRelease\n",
            "Hit:6 https://cloud.r-project.org/bin/linux/ubuntu jammy-cran40/ InRelease\n",
            "Hit:7 http://security.ubuntu.com/ubuntu jammy-security InRelease\n",
            "Hit:8 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy InRelease\n",
            "Hit:9 https://ppa.launchpadcontent.net/graphics-drivers/ppa/ubuntu jammy InRelease\n",
            "Hit:10 https://ppa.launchpadcontent.net/ubuntugis/ppa/ubuntu jammy InRelease\n",
            "Reading package lists... Done\n",
            "W: Skipping acquire of configured file 'main/source/Sources' as repository 'https://r2u.stat.illinois.edu/ubuntu jammy InRelease' does not seem to provide it (sources.list entry misspelt?)\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "chromium-chromedriver is already the newest version (1:85.0.4183.83-0ubuntu2.22.04.1).\n",
            "0 upgraded, 0 newly installed, 0 to remove and 31 not upgraded.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "\n",
        "# تنظیمات Chrome Options برای استفاده از headless\n",
        "options = Options()\n",
        "options.add_argument('--headless')  # حالت بدون رابط گرافیکی\n",
        "options.add_argument('--no-sandbox')\n",
        "options.add_argument('--disable-dev-shm-usage')\n",
        "options.add_argument('--remote-debugging-port=9222')\n",
        "\n",
        "# مسیر کروم در سرور گوگل کلب\n",
        "chrome_driver_path = '/usr/lib/chromium-browser/chromedriver'\n",
        "\n",
        "# راه‌اندازی WebDriver\n",
        "service = Service(chrome_driver_path)\n",
        "driver = webdriver.Chrome(service=service, options=options)\n",
        "\n",
        "# تست برای باز کردن سایت\n",
        "driver.get(\"https://www.google.com\")\n",
        "print(driver.title)  # چاپ عنوان صفحه\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 356
        },
        "id": "11d1IUSQe0ND",
        "outputId": "f2867362-e9b9-43ed-b4ce-516f43673da1"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "error",
          "ename": "WebDriverException",
          "evalue": "Message: Service /usr/lib/chromium-browser/chromedriver unexpectedly exited. Status code was: 1\n",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m                        Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-26-5f8c9c3551a2>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     15\u001b[0m \u001b[0;31m# راه‌اندازی WebDriver\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     16\u001b[0m \u001b[0mservice\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mService\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mchrome_driver_path\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 17\u001b[0;31m \u001b[0mdriver\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     18\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     19\u001b[0m \u001b[0;31m# تست برای باز کردن سایت\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chrome/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     43\u001b[0m         \u001b[0moptions\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0mOptions\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     44\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 45\u001b[0;31m         super().__init__(\n\u001b[0m\u001b[1;32m     46\u001b[0m             \u001b[0mbrowser_name\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mDesiredCapabilities\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCHROME\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"browserName\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     47\u001b[0m             \u001b[0mvendor_prefix\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"goog\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chromium/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, browser_name, vendor_prefix, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     53\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     54\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpath\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0menv_path\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0mfinder\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_driver_path\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 55\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     56\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     57\u001b[0m         executor = ChromiumRemoteConnection(\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/common/service.py\u001b[0m in \u001b[0;36mstart\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    111\u001b[0m         \u001b[0mcount\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    112\u001b[0m         \u001b[0;32mwhile\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 113\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0massert_process_still_running\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    114\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mis_connectable\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    115\u001b[0m                 \u001b[0;32mbreak\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/common/service.py\u001b[0m in \u001b[0;36massert_process_still_running\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    124\u001b[0m         \u001b[0mreturn_code\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mprocess\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpoll\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    125\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mreturn_code\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 126\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mWebDriverException\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mf\"Service {self._path} unexpectedly exited. Status code was: {return_code}\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    127\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    128\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mis_connectable\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m->\u001b[0m \u001b[0mbool\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mWebDriverException\u001b[0m: Message: Service /usr/lib/chromium-browser/chromedriver unexpectedly exited. Status code was: 1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# نصب نسخه‌های همخوان از Chromium و ChromeDriver\n",
        "!apt-get update # بروزرسانی پکیج‌ها\n",
        "!apt-get install -y chromium-browser\n",
        "!apt-get install -y chromium-chromedriver\n",
        "!pip install -q selenium\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Z5uze17Qe6Gz",
        "outputId": "d82d5d49-785f-4e6b-e825-32585573ea73"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\r0% [Working]\r            \rHit:1 https://cloud.r-project.org/bin/linux/ubuntu jammy-cran40/ InRelease\n",
            "\r0% [Connecting to archive.ubuntu.com (185.125.190.81)] [Waiting for headers] [Waiting for headers] [\r                                                                                                    \rHit:2 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64  InRelease\n",
            "Hit:3 https://r2u.stat.illinois.edu/ubuntu jammy InRelease\n",
            "Hit:4 http://security.ubuntu.com/ubuntu jammy-security InRelease\n",
            "Hit:5 http://archive.ubuntu.com/ubuntu jammy InRelease\n",
            "Hit:6 http://archive.ubuntu.com/ubuntu jammy-updates InRelease\n",
            "Hit:7 http://archive.ubuntu.com/ubuntu jammy-backports InRelease\n",
            "Hit:8 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy InRelease\n",
            "Hit:9 https://ppa.launchpadcontent.net/graphics-drivers/ppa/ubuntu jammy InRelease\n",
            "Hit:10 https://ppa.launchpadcontent.net/ubuntugis/ppa/ubuntu jammy InRelease\n",
            "Reading package lists... Done\n",
            "W: Skipping acquire of configured file 'main/source/Sources' as repository 'https://r2u.stat.illinois.edu/ubuntu jammy InRelease' does not seem to provide it (sources.list entry misspelt?)\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "chromium-browser is already the newest version (1:85.0.4183.83-0ubuntu2.22.04.1).\n",
            "chromium-browser set to manually installed.\n",
            "0 upgraded, 0 newly installed, 0 to remove and 31 not upgraded.\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "chromium-chromedriver is already the newest version (1:85.0.4183.83-0ubuntu2.22.04.1).\n",
            "0 upgraded, 0 newly installed, 0 to remove and 31 not upgraded.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "\n",
        "# تنظیمات Chrome Options برای استفاده از headless\n",
        "options = Options()\n",
        "options.add_argument('--headless')  # حالت بدون رابط گرافیکی\n",
        "options.add_argument('--no-sandbox')\n",
        "options.add_argument('--disable-dev-shm-usage')\n",
        "options.add_argument('--remote-debugging-port=9222')\n",
        "\n",
        "# مسیر کروم و کروم درایور\n",
        "chrome_driver_path = '/usr/lib/chromium-browser/chromedriver'\n",
        "chrome_path = '/usr/bin/chromium-browser'\n",
        "\n",
        "# تنظیم Service برای WebDriver\n",
        "service = Service(chrome_driver_path)\n",
        "\n",
        "# راه‌اندازی WebDriver\n",
        "driver = webdriver.Chrome(service=service, options=options)\n",
        "\n",
        "# باز کردن سایت و چاپ عنوان صفحه\n",
        "driver.get(\"https://www.google.com\")\n",
        "print(driver.title)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 356
        },
        "id": "RI1bqhIUe_hw",
        "outputId": "fae055fd-7092-4d13-bc9a-b20d6cd409d1"
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "error",
          "ename": "WebDriverException",
          "evalue": "Message: Service /usr/lib/chromium-browser/chromedriver unexpectedly exited. Status code was: 1\n",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m                        Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-28-977dc63e7a0c>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     18\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     19\u001b[0m \u001b[0;31m# راه‌اندازی WebDriver\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 20\u001b[0;31m \u001b[0mdriver\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     21\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     22\u001b[0m \u001b[0;31m# باز کردن سایت و چاپ عنوان صفحه\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chrome/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     43\u001b[0m         \u001b[0moptions\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0mOptions\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     44\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 45\u001b[0;31m         super().__init__(\n\u001b[0m\u001b[1;32m     46\u001b[0m             \u001b[0mbrowser_name\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mDesiredCapabilities\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCHROME\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"browserName\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     47\u001b[0m             \u001b[0mvendor_prefix\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"goog\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chromium/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, browser_name, vendor_prefix, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     53\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     54\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpath\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0menv_path\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0mfinder\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_driver_path\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 55\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     56\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     57\u001b[0m         executor = ChromiumRemoteConnection(\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/common/service.py\u001b[0m in \u001b[0;36mstart\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    111\u001b[0m         \u001b[0mcount\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    112\u001b[0m         \u001b[0;32mwhile\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 113\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0massert_process_still_running\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    114\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mis_connectable\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    115\u001b[0m                 \u001b[0;32mbreak\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/common/service.py\u001b[0m in \u001b[0;36massert_process_still_running\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    124\u001b[0m         \u001b[0mreturn_code\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mprocess\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpoll\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    125\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mreturn_code\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 126\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mWebDriverException\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mf\"Service {self._path} unexpectedly exited. Status code was: {return_code}\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    127\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    128\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mis_connectable\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m->\u001b[0m \u001b[0mbool\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mWebDriverException\u001b[0m: Message: Service /usr/lib/chromium-browser/chromedriver unexpectedly exited. Status code was: 1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# نصب و بروزرسانی chromium و chromedriver\n",
        "!apt-get update # بروزرسانی پکیج‌ها\n",
        "!apt-get install -y chromium-browser\n",
        "!apt-get install -y chromium-chromedriver\n",
        "!pip install -q selenium\n",
        "\n",
        "# بررسی نسخه‌های نصب‌شده chromium و chromedriver\n",
        "!which chromium-browser\n",
        "!chromium-browser --version\n",
        "!chromedriver --version\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_xXQSUXIfIgN",
        "outputId": "fe30cca1-4244-4237-d1c9-2f204b29c04c"
      },
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\r0% [Working]\r            \rHit:1 https://cloud.r-project.org/bin/linux/ubuntu jammy-cran40/ InRelease\n",
            "\r0% [Waiting for headers] [Connecting to security.ubuntu.com (185.125.190.82)] [Waiting for headers] \r                                                                                                    \rHit:2 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64  InRelease\n",
            "\r0% [Waiting for headers] [Connecting to security.ubuntu.com (185.125.190.82)] [Waiting for headers] \r                                                                                                    \rHit:3 https://r2u.stat.illinois.edu/ubuntu jammy InRelease\n",
            "Hit:4 http://archive.ubuntu.com/ubuntu jammy InRelease\n",
            "Hit:5 http://security.ubuntu.com/ubuntu jammy-security InRelease\n",
            "Hit:6 http://archive.ubuntu.com/ubuntu jammy-updates InRelease\n",
            "Hit:7 http://archive.ubuntu.com/ubuntu jammy-backports InRelease\n",
            "Hit:8 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy InRelease\n",
            "Hit:9 https://ppa.launchpadcontent.net/graphics-drivers/ppa/ubuntu jammy InRelease\n",
            "Hit:10 https://ppa.launchpadcontent.net/ubuntugis/ppa/ubuntu jammy InRelease\n",
            "Reading package lists... Done\n",
            "W: Skipping acquire of configured file 'main/source/Sources' as repository 'https://r2u.stat.illinois.edu/ubuntu jammy InRelease' does not seem to provide it (sources.list entry misspelt?)\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "chromium-browser is already the newest version (1:85.0.4183.83-0ubuntu2.22.04.1).\n",
            "0 upgraded, 0 newly installed, 0 to remove and 31 not upgraded.\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "chromium-chromedriver is already the newest version (1:85.0.4183.83-0ubuntu2.22.04.1).\n",
            "0 upgraded, 0 newly installed, 0 to remove and 31 not upgraded.\n",
            "/usr/bin/chromium-browser\n",
            "\n",
            "Command '/usr/bin/chromium-browser' requires the chromium snap to be installed.\n",
            "Please install it with:\n",
            "\n",
            "snap install chromium\n",
            "\n",
            "\n",
            "Command '/usr/bin/chromedriver' requires the chromium snap to be installed.\n",
            "Please install it with:\n",
            "\n",
            "snap install chromium\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "\n",
        "# تنظیمات Chrome Options برای استفاده از headless\n",
        "options = Options()\n",
        "options.add_argument('--headless')  # حالت بدون رابط گرافیکی\n",
        "options.add_argument('--no-sandbox')\n",
        "options.add_argument('--disable-dev-shm-usage')\n",
        "options.add_argument('--remote-debugging-port=9222')\n",
        "\n",
        "# مسیر کروم و کروم‌درایور\n",
        "chrome_driver_path = '/usr/lib/chromium-browser/chromedriver'\n",
        "chrome_path = '/usr/bin/chromium-browser'\n",
        "\n",
        "# تنظیم Service برای WebDriver\n",
        "service = Service(chrome_driver_path)\n",
        "\n",
        "# راه‌اندازی WebDriver\n",
        "driver = webdriver.Chrome(service=service, options=options)\n",
        "\n",
        "# باز کردن سایت و چاپ عنوان صفحه\n",
        "driver.get(\"https://www.google.com\")\n",
        "print(driver.title)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 356
        },
        "id": "qVu8PycyfXRy",
        "outputId": "376288ab-23e3-4529-8870-e2690e382b4f"
      },
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "error",
          "ename": "WebDriverException",
          "evalue": "Message: Service /usr/lib/chromium-browser/chromedriver unexpectedly exited. Status code was: 1\n",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m                        Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-30-a7852c8bf262>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     18\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     19\u001b[0m \u001b[0;31m# راه‌اندازی WebDriver\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 20\u001b[0;31m \u001b[0mdriver\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     21\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     22\u001b[0m \u001b[0;31m# باز کردن سایت و چاپ عنوان صفحه\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chrome/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     43\u001b[0m         \u001b[0moptions\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0mOptions\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     44\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 45\u001b[0;31m         super().__init__(\n\u001b[0m\u001b[1;32m     46\u001b[0m             \u001b[0mbrowser_name\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mDesiredCapabilities\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCHROME\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"browserName\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     47\u001b[0m             \u001b[0mvendor_prefix\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"goog\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chromium/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, browser_name, vendor_prefix, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     53\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     54\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpath\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0menv_path\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0mfinder\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_driver_path\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 55\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     56\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     57\u001b[0m         executor = ChromiumRemoteConnection(\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/common/service.py\u001b[0m in \u001b[0;36mstart\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    111\u001b[0m         \u001b[0mcount\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    112\u001b[0m         \u001b[0;32mwhile\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 113\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0massert_process_still_running\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    114\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mis_connectable\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    115\u001b[0m                 \u001b[0;32mbreak\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/common/service.py\u001b[0m in \u001b[0;36massert_process_still_running\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    124\u001b[0m         \u001b[0mreturn_code\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mprocess\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpoll\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    125\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mreturn_code\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 126\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mWebDriverException\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mf\"Service {self._path} unexpectedly exited. Status code was: {return_code}\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    127\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    128\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mis_connectable\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m->\u001b[0m \u001b[0mbool\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mWebDriverException\u001b[0m: Message: Service /usr/lib/chromium-browser/chromedriver unexpectedly exited. Status code was: 1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!apt-get update # بروزرسانی پکیج‌ها\n",
        "!apt-get install -y chromium-browser\n",
        "!apt-get install -y chromium-chromedriver\n",
        "!pip install -q selenium\n",
        "\n",
        "# بررسی نسخه‌های نصب‌شده chromium و chromedriver\n",
        "!which chromium-browser\n",
        "!chromium-browser --version\n",
        "!chromedriver --version\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Y7G8DdCdfdtp",
        "outputId": "035a0d54-38bb-43b5-953f-c4961d2f9783"
      },
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\r0% [Working]\r            \rHit:1 http://security.ubuntu.com/ubuntu jammy-security InRelease\n",
            "\r0% [Connecting to archive.ubuntu.com (185.125.190.81)] [Connected to cloud.r-project.org (18.160.213\r                                                                                                    \rHit:2 https://cloud.r-project.org/bin/linux/ubuntu jammy-cran40/ InRelease\n",
            "Hit:3 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64  InRelease\n",
            "Hit:4 https://r2u.stat.illinois.edu/ubuntu jammy InRelease\n",
            "Hit:5 http://archive.ubuntu.com/ubuntu jammy InRelease\n",
            "Hit:6 http://archive.ubuntu.com/ubuntu jammy-updates InRelease\n",
            "Hit:7 http://archive.ubuntu.com/ubuntu jammy-backports InRelease\n",
            "Hit:8 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy InRelease\n",
            "Hit:9 https://ppa.launchpadcontent.net/graphics-drivers/ppa/ubuntu jammy InRelease\n",
            "Hit:10 https://ppa.launchpadcontent.net/ubuntugis/ppa/ubuntu jammy InRelease\n",
            "Reading package lists... Done\n",
            "W: Skipping acquire of configured file 'main/source/Sources' as repository 'https://r2u.stat.illinois.edu/ubuntu jammy InRelease' does not seem to provide it (sources.list entry misspelt?)\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "chromium-browser is already the newest version (1:85.0.4183.83-0ubuntu2.22.04.1).\n",
            "0 upgraded, 0 newly installed, 0 to remove and 31 not upgraded.\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "chromium-chromedriver is already the newest version (1:85.0.4183.83-0ubuntu2.22.04.1).\n",
            "0 upgraded, 0 newly installed, 0 to remove and 31 not upgraded.\n",
            "/usr/bin/chromium-browser\n",
            "\n",
            "Command '/usr/bin/chromium-browser' requires the chromium snap to be installed.\n",
            "Please install it with:\n",
            "\n",
            "snap install chromium\n",
            "\n",
            "\n",
            "Command '/usr/bin/chromedriver' requires the chromium snap to be installed.\n",
            "Please install it with:\n",
            "\n",
            "snap install chromium\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "\n",
        "# تنظیمات Chrome Options برای استفاده از headless\n",
        "options = Options()\n",
        "options.add_argument('--headless')  # حالت بدون رابط گرافیکی\n",
        "options.add_argument('--no-sandbox')\n",
        "options.add_argument('--disable-dev-shm-usage')\n",
        "options.add_argument('--remote-debugging-port=9222')\n",
        "\n",
        "# مسیر کروم و کروم‌درایور\n",
        "chrome_driver_path = '/usr/lib/chromium-browser/chromedriver'\n",
        "chrome_path = '/usr/bin/chromium-browser'\n",
        "\n",
        "# تنظیمات سرویس برای WebDriver\n",
        "service = Service(chrome_driver_path)\n",
        "\n",
        "# راه‌اندازی WebDriver\n",
        "driver = webdriver.Chrome(service=service, options=options)\n",
        "\n",
        "# باز کردن سایت و چاپ عنوان صفحه\n",
        "driver.get(\"https://www.google.com\")\n",
        "print(driver.title)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 356
        },
        "id": "pt7sYmbqfj4K",
        "outputId": "8a5db4d5-90cf-4c5d-8727-166d9645cd78"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "error",
          "ename": "WebDriverException",
          "evalue": "Message: Service /usr/lib/chromium-browser/chromedriver unexpectedly exited. Status code was: 1\n",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m                        Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-32-88c965179a45>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     18\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     19\u001b[0m \u001b[0;31m# راه‌اندازی WebDriver\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 20\u001b[0;31m \u001b[0mdriver\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     21\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     22\u001b[0m \u001b[0;31m# باز کردن سایت و چاپ عنوان صفحه\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chrome/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     43\u001b[0m         \u001b[0moptions\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0mOptions\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     44\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 45\u001b[0;31m         super().__init__(\n\u001b[0m\u001b[1;32m     46\u001b[0m             \u001b[0mbrowser_name\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mDesiredCapabilities\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCHROME\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"browserName\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     47\u001b[0m             \u001b[0mvendor_prefix\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"goog\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chromium/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, browser_name, vendor_prefix, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     53\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     54\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpath\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0menv_path\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0mfinder\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_driver_path\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 55\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     56\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     57\u001b[0m         executor = ChromiumRemoteConnection(\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/common/service.py\u001b[0m in \u001b[0;36mstart\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    111\u001b[0m         \u001b[0mcount\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    112\u001b[0m         \u001b[0;32mwhile\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 113\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0massert_process_still_running\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    114\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mis_connectable\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    115\u001b[0m                 \u001b[0;32mbreak\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/common/service.py\u001b[0m in \u001b[0;36massert_process_still_running\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    124\u001b[0m         \u001b[0mreturn_code\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mprocess\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpoll\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    125\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mreturn_code\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 126\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mWebDriverException\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mf\"Service {self._path} unexpectedly exited. Status code was: {return_code}\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    127\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    128\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mis_connectable\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m->\u001b[0m \u001b[0mbool\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mWebDriverException\u001b[0m: Message: Service /usr/lib/chromium-browser/chromedriver unexpectedly exited. Status code was: 1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import time\n",
        "try:\n",
        "    driver = webdriver.Chrome(service=service, options=options)\n",
        "    driver.get(\"https://www.google.com\")\n",
        "    print(driver.title)\n",
        "except Exception as e:\n",
        "    print(f\"Error: {e}\")\n",
        "    time.sleep(5)\n",
        "    driver.quit()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Oxhe8xkBflxD",
        "outputId": "dfca91a1-13b5-499c-ab36-fe8c6ff58db5"
      },
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Error: Message: Service /usr/lib/chromium-browser/chromedriver unexpectedly exited. Status code was: 1\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# بروزرسانی پکیج‌ها و نصب Chromium و Chromedriver\n",
        "!apt-get update -y\n",
        "!apt-get install -y chromium-browser\n",
        "!apt-get install -y chromium-chromedriver\n",
        "\n",
        "# نصب Selenium\n",
        "!pip install -q selenium\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Zam6Mp9Hft1N",
        "outputId": "447cdebe-eab2-40e0-f368-a140b214a39c"
      },
      "execution_count": 34,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\r0% [Working]\r            \rHit:1 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64  InRelease\n",
            "\r0% [Connecting to archive.ubuntu.com (91.189.91.83)] [Connecting to security.ubuntu.com (91.189.91.8\r                                                                                                    \rHit:2 https://cloud.r-project.org/bin/linux/ubuntu jammy-cran40/ InRelease\n",
            "Hit:3 https://r2u.stat.illinois.edu/ubuntu jammy InRelease\n",
            "Hit:4 http://security.ubuntu.com/ubuntu jammy-security InRelease\n",
            "Hit:5 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy InRelease\n",
            "Hit:6 http://archive.ubuntu.com/ubuntu jammy InRelease\n",
            "Hit:7 https://ppa.launchpadcontent.net/graphics-drivers/ppa/ubuntu jammy InRelease\n",
            "Hit:8 http://archive.ubuntu.com/ubuntu jammy-updates InRelease\n",
            "Hit:9 https://ppa.launchpadcontent.net/ubuntugis/ppa/ubuntu jammy InRelease\n",
            "Hit:10 http://archive.ubuntu.com/ubuntu jammy-backports InRelease\n",
            "Reading package lists... Done\n",
            "W: Skipping acquire of configured file 'main/source/Sources' as repository 'https://r2u.stat.illinois.edu/ubuntu jammy InRelease' does not seem to provide it (sources.list entry misspelt?)\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "chromium-browser is already the newest version (1:85.0.4183.83-0ubuntu2.22.04.1).\n",
            "0 upgraded, 0 newly installed, 0 to remove and 31 not upgraded.\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "chromium-chromedriver is already the newest version (1:85.0.4183.83-0ubuntu2.22.04.1).\n",
            "0 upgraded, 0 newly installed, 0 to remove and 31 not upgraded.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# بررسی مسیرهای نصب‌شده\n",
        "!which chromium-browser\n",
        "!chromium-browser --version\n",
        "!chromedriver --version\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4wbTbSH8fyOr",
        "outputId": "afe84c42-f01b-4fda-f0b5-440a8aeafd3e"
      },
      "execution_count": 35,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/usr/bin/chromium-browser\n",
            "\n",
            "Command '/usr/bin/chromium-browser' requires the chromium snap to be installed.\n",
            "Please install it with:\n",
            "\n",
            "snap install chromium\n",
            "\n",
            "\n",
            "Command '/usr/bin/chromedriver' requires the chromium snap to be installed.\n",
            "Please install it with:\n",
            "\n",
            "snap install chromium\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "\n",
        "# تنظیمات Chrome Options برای استفاده از headless\n",
        "options = Options()\n",
        "options.add_argument('--headless')  # حالت بدون رابط گرافیکی\n",
        "options.add_argument('--no-sandbox')\n",
        "options.add_argument('--disable-dev-shm-usage')\n",
        "options.add_argument('--remote-debugging-port=9222')\n",
        "\n",
        "# مسیرهای صحیح Chromium و Chromedriver در Colab\n",
        "chrome_driver_path = '/usr/lib/chromium-browser/chromedriver'\n",
        "chrome_path = '/usr/bin/chromium-browser'\n",
        "\n",
        "# تنظیمات سرویس برای WebDriver\n",
        "service = Service(chrome_driver_path)\n",
        "\n",
        "# راه‌اندازی WebDriver\n",
        "driver = webdriver.Chrome(service=service, options=options)\n",
        "\n",
        "# باز کردن سایت و چاپ عنوان صفحه\n",
        "driver.get(\"https://www.google.com\")\n",
        "print(driver.title)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 356
        },
        "id": "G7cIqv2sf1Zk",
        "outputId": "da7f148d-8903-414a-cc87-73dbbe28e658"
      },
      "execution_count": 36,
      "outputs": [
        {
          "output_type": "error",
          "ename": "WebDriverException",
          "evalue": "Message: Service /usr/lib/chromium-browser/chromedriver unexpectedly exited. Status code was: 1\n",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m                        Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-36-8b1224e57cce>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     18\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     19\u001b[0m \u001b[0;31m# راه‌اندازی WebDriver\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 20\u001b[0;31m \u001b[0mdriver\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     21\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     22\u001b[0m \u001b[0;31m# باز کردن سایت و چاپ عنوان صفحه\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chrome/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     43\u001b[0m         \u001b[0moptions\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0mOptions\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     44\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 45\u001b[0;31m         super().__init__(\n\u001b[0m\u001b[1;32m     46\u001b[0m             \u001b[0mbrowser_name\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mDesiredCapabilities\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCHROME\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"browserName\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     47\u001b[0m             \u001b[0mvendor_prefix\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"goog\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chromium/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, browser_name, vendor_prefix, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     53\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     54\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpath\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0menv_path\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0mfinder\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_driver_path\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 55\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     56\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     57\u001b[0m         executor = ChromiumRemoteConnection(\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/common/service.py\u001b[0m in \u001b[0;36mstart\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    111\u001b[0m         \u001b[0mcount\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    112\u001b[0m         \u001b[0;32mwhile\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 113\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0massert_process_still_running\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    114\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mis_connectable\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    115\u001b[0m                 \u001b[0;32mbreak\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/common/service.py\u001b[0m in \u001b[0;36massert_process_still_running\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    124\u001b[0m         \u001b[0mreturn_code\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mprocess\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpoll\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    125\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mreturn_code\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 126\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mWebDriverException\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mf\"Service {self._path} unexpectedly exited. Status code was: {return_code}\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    127\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    128\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mis_connectable\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m->\u001b[0m \u001b[0mbool\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mWebDriverException\u001b[0m: Message: Service /usr/lib/chromium-browser/chromedriver unexpectedly exited. Status code was: 1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# بروزرسانی پکیج‌ها\n",
        "!apt-get update -y\n",
        "\n",
        "# نصب chromium-browser\n",
        "!apt-get install -y chromium-browser\n",
        "\n",
        "# نصب chromedriver\n",
        "!apt-get install -y chromium-chromedriver\n",
        "\n",
        "# نصب Selenium\n",
        "!pip install -q selenium\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0nHUi-tVf87l",
        "outputId": "1ccbe0b1-2384-445f-9257-3068dd895494"
      },
      "execution_count": 37,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\r0% [Working]\r            \rHit:1 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64  InRelease\n",
            "\r0% [Waiting for headers] [Connecting to security.ubuntu.com] [Connected to cloud.r-project.org (18.1\r                                                                                                    \rHit:2 https://cloud.r-project.org/bin/linux/ubuntu jammy-cran40/ InRelease\n",
            "Hit:3 http://security.ubuntu.com/ubuntu jammy-security InRelease\n",
            "Hit:4 https://r2u.stat.illinois.edu/ubuntu jammy InRelease\n",
            "Hit:5 http://archive.ubuntu.com/ubuntu jammy InRelease\n",
            "Hit:6 http://archive.ubuntu.com/ubuntu jammy-updates InRelease\n",
            "Hit:7 http://archive.ubuntu.com/ubuntu jammy-backports InRelease\n",
            "Hit:8 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy InRelease\n",
            "Hit:9 https://ppa.launchpadcontent.net/graphics-drivers/ppa/ubuntu jammy InRelease\n",
            "Hit:10 https://ppa.launchpadcontent.net/ubuntugis/ppa/ubuntu jammy InRelease\n",
            "Reading package lists... Done\n",
            "W: Skipping acquire of configured file 'main/source/Sources' as repository 'https://r2u.stat.illinois.edu/ubuntu jammy InRelease' does not seem to provide it (sources.list entry misspelt?)\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "chromium-browser is already the newest version (1:85.0.4183.83-0ubuntu2.22.04.1).\n",
            "0 upgraded, 0 newly installed, 0 to remove and 31 not upgraded.\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "chromium-chromedriver is already the newest version (1:85.0.4183.83-0ubuntu2.22.04.1).\n",
            "0 upgraded, 0 newly installed, 0 to remove and 31 not upgraded.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "\n",
        "# تنظیمات Chrome Options برای استفاده از headless\n",
        "options = Options()\n",
        "options.add_argument('--headless')  # حالت بدون رابط گرافیکی\n",
        "options.add_argument('--no-sandbox')\n",
        "options.add_argument('--disable-dev-shm-usage')\n",
        "options.add_argument('--remote-debugging-port=9222')\n",
        "\n",
        "# مسیرهای صحیح Chromium و Chromedriver در Colab\n",
        "chrome_driver_path = '/usr/lib/chromium-browser/chromedriver'\n",
        "chrome_path = '/usr/bin/chromium-browser'\n",
        "\n",
        "# تنظیمات سرویس برای WebDriver\n",
        "service = Service(chrome_driver_path)\n",
        "\n",
        "# راه‌اندازی WebDriver\n",
        "driver = webdriver.Chrome(service=service, options=options)\n",
        "\n",
        "# باز کردن سایت و چاپ عنوان صفحه\n",
        "driver.get(\"https://www.google.com\")\n",
        "print(driver.title)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 356
        },
        "id": "5VBTZ8eDgB1I",
        "outputId": "cebc3b94-350b-427b-8c0c-385bb8143fde"
      },
      "execution_count": 38,
      "outputs": [
        {
          "output_type": "error",
          "ename": "WebDriverException",
          "evalue": "Message: Service /usr/lib/chromium-browser/chromedriver unexpectedly exited. Status code was: 1\n",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m                        Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-38-8b1224e57cce>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     18\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     19\u001b[0m \u001b[0;31m# راه‌اندازی WebDriver\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 20\u001b[0;31m \u001b[0mdriver\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     21\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     22\u001b[0m \u001b[0;31m# باز کردن سایت و چاپ عنوان صفحه\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chrome/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     43\u001b[0m         \u001b[0moptions\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0mOptions\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     44\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 45\u001b[0;31m         super().__init__(\n\u001b[0m\u001b[1;32m     46\u001b[0m             \u001b[0mbrowser_name\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mDesiredCapabilities\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCHROME\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"browserName\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     47\u001b[0m             \u001b[0mvendor_prefix\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"goog\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chromium/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, browser_name, vendor_prefix, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     53\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     54\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpath\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0menv_path\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0mfinder\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_driver_path\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 55\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     56\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     57\u001b[0m         executor = ChromiumRemoteConnection(\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/common/service.py\u001b[0m in \u001b[0;36mstart\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    111\u001b[0m         \u001b[0mcount\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    112\u001b[0m         \u001b[0;32mwhile\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 113\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0massert_process_still_running\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    114\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mis_connectable\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    115\u001b[0m                 \u001b[0;32mbreak\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/common/service.py\u001b[0m in \u001b[0;36massert_process_still_running\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    124\u001b[0m         \u001b[0mreturn_code\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mprocess\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpoll\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    125\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mreturn_code\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 126\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mWebDriverException\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mf\"Service {self._path} unexpectedly exited. Status code was: {return_code}\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    127\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    128\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mis_connectable\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m->\u001b[0m \u001b[0mbool\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mWebDriverException\u001b[0m: Message: Service /usr/lib/chromium-browser/chromedriver unexpectedly exited. Status code was: 1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# نصب Chromium و وابستگی‌ها\n",
        "!apt-get update -y\n",
        "!apt-get install -y chromium-browser\n",
        "!apt-get install -y chromium-chromedriver\n",
        "\n",
        "# نصب سایر وابستگی‌ها\n",
        "!apt-get install -y libappindicator3-1 libindicator3-1\n",
        "!apt-get install -y fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RN09-F9wgLnB",
        "outputId": "7bb1aa1f-69d4-47bd-d0c1-99c18579159d"
      },
      "execution_count": 39,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hit:1 https://cloud.r-project.org/bin/linux/ubuntu jammy-cran40/ InRelease\n",
            "Hit:2 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64  InRelease\n",
            "Hit:3 http://security.ubuntu.com/ubuntu jammy-security InRelease\n",
            "Hit:4 https://r2u.stat.illinois.edu/ubuntu jammy InRelease\n",
            "Hit:5 http://archive.ubuntu.com/ubuntu jammy InRelease\n",
            "Hit:6 http://archive.ubuntu.com/ubuntu jammy-updates InRelease\n",
            "Hit:7 http://archive.ubuntu.com/ubuntu jammy-backports InRelease\n",
            "Hit:8 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy InRelease\n",
            "Hit:9 https://ppa.launchpadcontent.net/graphics-drivers/ppa/ubuntu jammy InRelease\n",
            "Hit:10 https://ppa.launchpadcontent.net/ubuntugis/ppa/ubuntu jammy InRelease\n",
            "Reading package lists... Done\n",
            "W: Skipping acquire of configured file 'main/source/Sources' as repository 'https://r2u.stat.illinois.edu/ubuntu jammy InRelease' does not seem to provide it (sources.list entry misspelt?)\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "chromium-browser is already the newest version (1:85.0.4183.83-0ubuntu2.22.04.1).\n",
            "0 upgraded, 0 newly installed, 0 to remove and 31 not upgraded.\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "chromium-chromedriver is already the newest version (1:85.0.4183.83-0ubuntu2.22.04.1).\n",
            "0 upgraded, 0 newly installed, 0 to remove and 31 not upgraded.\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "E: Unable to locate package libindicator3-1\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "fonts-liberation is already the newest version (1:1.07.4-11).\n",
            "lsb-release is already the newest version (11.1.0ubuntu4).\n",
            "lsb-release set to manually installed.\n",
            "libnss3 is already the newest version (2:3.98-0ubuntu0.22.04.2).\n",
            "libnss3 set to manually installed.\n",
            "xdg-utils is already the newest version (1.1.3-4.1ubuntu3~22.04.1).\n",
            "xdg-utils set to manually installed.\n",
            "The following additional packages will be installed:\n",
            "  libdbusmenu-glib4 libdbusmenu-gtk4 libgail-common libgail18 libgtk2.0-0 libgtk2.0-bin\n",
            "  libgtk2.0-common librsvg2-common\n",
            "Suggested packages:\n",
            "  indicator-application gvfs\n",
            "The following NEW packages will be installed:\n",
            "  libappindicator1 libdbusmenu-glib4 libdbusmenu-gtk4 libgail-common libgail18 libgtk2.0-0\n",
            "  libgtk2.0-bin libgtk2.0-common librsvg2-common\n",
            "0 upgraded, 9 newly installed, 0 to remove and 31 not upgraded.\n",
            "Need to get 2,436 kB of archives.\n",
            "After this operation, 7,610 kB of additional disk space will be used.\n",
            "Get:1 http://archive.ubuntu.com/ubuntu jammy/main amd64 libdbusmenu-glib4 amd64 16.04.1+18.10.20180917-0ubuntu8 [45.4 kB]\n",
            "Get:2 http://archive.ubuntu.com/ubuntu jammy/universe amd64 libdbusmenu-gtk4 amd64 16.04.1+18.10.20180917-0ubuntu8 [30.9 kB]\n",
            "Get:3 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libgtk2.0-common all 2.24.33-2ubuntu2.1 [125 kB]\n",
            "Get:4 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libgtk2.0-0 amd64 2.24.33-2ubuntu2.1 [2,038 kB]\n",
            "Get:5 http://archive.ubuntu.com/ubuntu jammy/universe amd64 libappindicator1 amd64 12.10.1+20.10.20200706.1-0ubuntu1 [23.1 kB]\n",
            "Get:6 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libgail18 amd64 2.24.33-2ubuntu2.1 [15.9 kB]\n",
            "Get:7 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libgail-common amd64 2.24.33-2ubuntu2.1 [132 kB]\n",
            "Get:8 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libgtk2.0-bin amd64 2.24.33-2ubuntu2.1 [7,936 B]\n",
            "Get:9 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 librsvg2-common amd64 2.52.5+dfsg-3ubuntu0.2 [17.7 kB]\n",
            "Fetched 2,436 kB in 1s (2,119 kB/s)\n",
            "Selecting previously unselected package libdbusmenu-glib4:amd64.\n",
            "(Reading database ... 125412 files and directories currently installed.)\n",
            "Preparing to unpack .../0-libdbusmenu-glib4_16.04.1+18.10.20180917-0ubuntu8_amd64.deb ...\n",
            "Unpacking libdbusmenu-glib4:amd64 (16.04.1+18.10.20180917-0ubuntu8) ...\n",
            "Selecting previously unselected package libdbusmenu-gtk4:amd64.\n",
            "Preparing to unpack .../1-libdbusmenu-gtk4_16.04.1+18.10.20180917-0ubuntu8_amd64.deb ...\n",
            "Unpacking libdbusmenu-gtk4:amd64 (16.04.1+18.10.20180917-0ubuntu8) ...\n",
            "Selecting previously unselected package libgtk2.0-common.\n",
            "Preparing to unpack .../2-libgtk2.0-common_2.24.33-2ubuntu2.1_all.deb ...\n",
            "Unpacking libgtk2.0-common (2.24.33-2ubuntu2.1) ...\n",
            "Selecting previously unselected package libgtk2.0-0:amd64.\n",
            "Preparing to unpack .../3-libgtk2.0-0_2.24.33-2ubuntu2.1_amd64.deb ...\n",
            "Unpacking libgtk2.0-0:amd64 (2.24.33-2ubuntu2.1) ...\n",
            "Selecting previously unselected package libappindicator1.\n",
            "Preparing to unpack .../4-libappindicator1_12.10.1+20.10.20200706.1-0ubuntu1_amd64.deb ...\n",
            "Unpacking libappindicator1 (12.10.1+20.10.20200706.1-0ubuntu1) ...\n",
            "Selecting previously unselected package libgail18:amd64.\n",
            "Preparing to unpack .../5-libgail18_2.24.33-2ubuntu2.1_amd64.deb ...\n",
            "Unpacking libgail18:amd64 (2.24.33-2ubuntu2.1) ...\n",
            "Selecting previously unselected package libgail-common:amd64.\n",
            "Preparing to unpack .../6-libgail-common_2.24.33-2ubuntu2.1_amd64.deb ...\n",
            "Unpacking libgail-common:amd64 (2.24.33-2ubuntu2.1) ...\n",
            "Selecting previously unselected package libgtk2.0-bin.\n",
            "Preparing to unpack .../7-libgtk2.0-bin_2.24.33-2ubuntu2.1_amd64.deb ...\n",
            "Unpacking libgtk2.0-bin (2.24.33-2ubuntu2.1) ...\n",
            "Selecting previously unselected package librsvg2-common:amd64.\n",
            "Preparing to unpack .../8-librsvg2-common_2.52.5+dfsg-3ubuntu0.2_amd64.deb ...\n",
            "Unpacking librsvg2-common:amd64 (2.52.5+dfsg-3ubuntu0.2) ...\n",
            "Setting up libdbusmenu-glib4:amd64 (16.04.1+18.10.20180917-0ubuntu8) ...\n",
            "Setting up librsvg2-common:amd64 (2.52.5+dfsg-3ubuntu0.2) ...\n",
            "Setting up libgtk2.0-common (2.24.33-2ubuntu2.1) ...\n",
            "Setting up libdbusmenu-gtk4:amd64 (16.04.1+18.10.20180917-0ubuntu8) ...\n",
            "Setting up libgtk2.0-0:amd64 (2.24.33-2ubuntu2.1) ...\n",
            "Setting up libappindicator1 (12.10.1+20.10.20200706.1-0ubuntu1) ...\n",
            "Setting up libgail18:amd64 (2.24.33-2ubuntu2.1) ...\n",
            "Setting up libgtk2.0-bin (2.24.33-2ubuntu2.1) ...\n",
            "Setting up libgail-common:amd64 (2.24.33-2ubuntu2.1) ...\n",
            "Processing triggers for man-db (2.10.2-1) ...\n",
            "Processing triggers for libgdk-pixbuf-2.0-0:amd64 (2.42.8+dfsg-1ubuntu0.3) ...\n",
            "Processing triggers for libc-bin (2.35-0ubuntu3.8) ...\n",
            "/sbin/ldconfig.real: /usr/local/lib/libur_adapter_level_zero.so.0 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtbbmalloc.so.2 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libhwloc.so.15 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtcm.so.1 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtbb.so.12 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtbbbind_2_5.so.3 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libur_adapter_opencl.so.0 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtbbmalloc_proxy.so.2 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libur_loader.so.0 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libumf.so.0 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtbbbind_2_0.so.3 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtbbbind.so.3 is not a symbolic link\n",
            "\n",
            "/sbin/ldconfig.real: /usr/local/lib/libtcm_debug.so.1 is not a symbolic link\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "\n",
        "# تنظیمات Chrome Options برای استفاده از headless\n",
        "options = Options()\n",
        "options.add_argument('--headless')  # حالت بدون رابط گرافیکی\n",
        "options.add_argument('--no-sandbox')\n",
        "options.add_argument('--disable-dev-shm-usage')\n",
        "options.add_argument('--remote-debugging-port=9222')\n",
        "\n",
        "# مسیرهای صحیح Chromium و Chromedriver\n",
        "chrome_driver_path = '/usr/lib/chromium-browser/chromedriver'\n",
        "chrome_path = '/usr/bin/chromium-browser'\n",
        "\n",
        "# تنظیمات سرویس برای WebDriver\n",
        "service = Service(chrome_driver_path)\n",
        "\n",
        "# راه‌اندازی WebDriver\n",
        "driver = webdriver.Chrome(service=service, options=options)\n",
        "\n",
        "# باز کردن سایت و چاپ عنوان صفحه\n",
        "driver.get(\"https://www.google.com\")\n",
        "print(driver.title)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 356
        },
        "id": "RTa_IZBigUcq",
        "outputId": "d4b0f2a6-f38c-4344-e367-761dadf5536d"
      },
      "execution_count": 40,
      "outputs": [
        {
          "output_type": "error",
          "ename": "WebDriverException",
          "evalue": "Message: Service /usr/lib/chromium-browser/chromedriver unexpectedly exited. Status code was: 1\n",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m                        Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-40-b7842857ebae>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     18\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     19\u001b[0m \u001b[0;31m# راه‌اندازی WebDriver\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 20\u001b[0;31m \u001b[0mdriver\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     21\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     22\u001b[0m \u001b[0;31m# باز کردن سایت و چاپ عنوان صفحه\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chrome/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     43\u001b[0m         \u001b[0moptions\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0mOptions\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     44\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 45\u001b[0;31m         super().__init__(\n\u001b[0m\u001b[1;32m     46\u001b[0m             \u001b[0mbrowser_name\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mDesiredCapabilities\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCHROME\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"browserName\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     47\u001b[0m             \u001b[0mvendor_prefix\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"goog\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chromium/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, browser_name, vendor_prefix, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     53\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     54\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpath\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0menv_path\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0mfinder\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_driver_path\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 55\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     56\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     57\u001b[0m         executor = ChromiumRemoteConnection(\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/common/service.py\u001b[0m in \u001b[0;36mstart\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    111\u001b[0m         \u001b[0mcount\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    112\u001b[0m         \u001b[0;32mwhile\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 113\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0massert_process_still_running\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    114\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mis_connectable\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    115\u001b[0m                 \u001b[0;32mbreak\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/common/service.py\u001b[0m in \u001b[0;36massert_process_still_running\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    124\u001b[0m         \u001b[0mreturn_code\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mprocess\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpoll\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    125\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mreturn_code\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 126\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mWebDriverException\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mf\"Service {self._path} unexpectedly exited. Status code was: {return_code}\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    127\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    128\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mis_connectable\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m->\u001b[0m \u001b[0mbool\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mWebDriverException\u001b[0m: Message: Service /usr/lib/chromium-browser/chromedriver unexpectedly exited. Status code was: 1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# دانلود ورژن خاص chromedriver\n",
        "!wget https://chromedriver.storage.googleapis.com/113.0.5672.63/chromedriver_linux64.zip\n",
        "!unzip chromedriver_linux64.zip\n",
        "!mv chromedriver /usr/bin/chromedriver\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "r-Bp8THEgW8a",
        "outputId": "bbdaacd2-6c05-47ba-fd6b-ac1524d227cb"
      },
      "execution_count": 41,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "--2025-03-11 14:00:05--  https://chromedriver.storage.googleapis.com/113.0.5672.63/chromedriver_linux64.zip\n",
            "Resolving chromedriver.storage.googleapis.com (chromedriver.storage.googleapis.com)... 142.251.183.207, 108.177.121.207, 209.85.145.207, ...\n",
            "Connecting to chromedriver.storage.googleapis.com (chromedriver.storage.googleapis.com)|142.251.183.207|:443... connected.\n",
            "HTTP request sent, awaiting response... 200 OK\n",
            "Length: 7315061 (7.0M) [application/zip]\n",
            "Saving to: ‘chromedriver_linux64.zip’\n",
            "\n",
            "\rchromedriver_linux6   0%[                    ]       0  --.-KB/s               \rchromedriver_linux6 100%[===================>]   6.98M  --.-KB/s    in 0.06s   \n",
            "\n",
            "2025-03-11 14:00:05 (126 MB/s) - ‘chromedriver_linux64.zip’ saved [7315061/7315061]\n",
            "\n",
            "Archive:  chromedriver_linux64.zip\n",
            "  inflating: chromedriver            \n",
            "  inflating: LICENSE.chromedriver    \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!mv chromedriver /usr/bin/chromedriver\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FWpnNCXlgchb",
        "outputId": "f48ef4b6-9a67-40d3-fabd-0cbf39409e13"
      },
      "execution_count": 42,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "mv: cannot stat 'chromedriver': No such file or directory\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!chmod +x /usr/bin/chromedriver"
      ],
      "metadata": {
        "id": "bpFZTqHZgeff"
      },
      "execution_count": 43,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "\n",
        "# تنظیمات Chrome Options برای استفاده از headless\n",
        "options = Options()\n",
        "options.add_argument('--headless')  # حالت بدون رابط گرافیکی\n",
        "options.add_argument('--no-sandbox')\n",
        "options.add_argument('--disable-dev-shm-usage')\n",
        "options.add_argument('--remote-debugging-port=9222')\n",
        "\n",
        "# مسیرهای صحیح Chromium و Chromedriver\n",
        "chrome_driver_path = '/usr/bin/chromedriver'\n",
        "chrome_path = '/usr/bin/chromium-browser'\n",
        "\n",
        "# تنظیمات سرویس برای WebDriver\n",
        "service = Service(chrome_driver_path)\n",
        "\n",
        "# راه‌اندازی WebDriver\n",
        "driver = webdriver.Chrome(service=service, options=options)\n",
        "\n",
        "# باز کردن سایت و چاپ عنوان صفحه\n",
        "driver.get(\"https://www.google.com\")\n",
        "print(driver.title)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 686
        },
        "id": "hI2dRLTIgkbC",
        "outputId": "17fe9ac1-756f-4330-f0ae-62baeabb91e3"
      },
      "execution_count": 44,
      "outputs": [
        {
          "output_type": "error",
          "ename": "WebDriverException",
          "evalue": "Message: unknown error: Chrome failed to start: exited abnormally.\n  (chrome not reachable)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x5cae5a47a133 <unknown>\n#1 0x5cae5a1ae966 <unknown>\n#2 0x5cae5a1d821a <unknown>\n#3 0x5cae5a1d407b <unknown>\n#4 0x5cae5a2139ad <unknown>\n#5 0x5cae5a21318f <unknown>\n#6 0x5cae5a20a9a3 <unknown>\n#7 0x5cae5a1df46a <unknown>\n#8 0x5cae5a1e055e <unknown>\n#9 0x5cae5a439cae <unknown>\n#10 0x5cae5a43d8fe <unknown>\n#11 0x5cae5a446f20 <unknown>\n#12 0x5cae5a43e923 <unknown>\n#13 0x5cae5a411c0e <unknown>\n#14 0x5cae5a461b08 <unknown>\n#15 0x5cae5a461c97 <unknown>\n#16 0x5cae5a472113 <unknown>\n#17 0x7d5e42a95ac3 <unknown>\n",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m                        Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-44-1f525cb857b7>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     18\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     19\u001b[0m \u001b[0;31m# راه‌اندازی WebDriver\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 20\u001b[0;31m \u001b[0mdriver\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     21\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     22\u001b[0m \u001b[0;31m# باز کردن سایت و چاپ عنوان صفحه\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chrome/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     43\u001b[0m         \u001b[0moptions\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0mOptions\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     44\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 45\u001b[0;31m         super().__init__(\n\u001b[0m\u001b[1;32m     46\u001b[0m             \u001b[0mbrowser_name\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mDesiredCapabilities\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCHROME\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"browserName\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     47\u001b[0m             \u001b[0mvendor_prefix\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"goog\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chromium/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, browser_name, vendor_prefix, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     64\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     65\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 66\u001b[0;31m             \u001b[0msuper\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__init__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mexecutor\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     67\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     68\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mquit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, command_executor, keep_alive, file_detector, options, locator_converter, web_element_cls, client_config)\u001b[0m\n\u001b[1;32m    248\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_authenticator_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    249\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_client\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 250\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_session\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    251\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_fedcm\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mFedCM\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    252\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mstart_session\u001b[0;34m(self, capabilities)\u001b[0m\n\u001b[1;32m    340\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    341\u001b[0m         \u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_create_caps\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 342\u001b[0;31m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mCommand\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mNEW_SESSION\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcaps\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    343\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msession_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"sessionId\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    344\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"capabilities\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, driver_command, params)\u001b[0m\n\u001b[1;32m    427\u001b[0m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    428\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 429\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    430\u001b[0m             \u001b[0mresponse\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_unwrap_value\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    431\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/errorhandler.py\u001b[0m in \u001b[0;36mcheck_response\u001b[0;34m(self, response)\u001b[0m\n\u001b[1;32m    230\u001b[0m                 \u001b[0malert_text\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"alert\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"text\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    231\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0malert_text\u001b[0m\u001b[0;34m)\u001b[0m  \u001b[0;31m# type: ignore[call-arg]  # mypy is not smart enough here\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 232\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m: Message: unknown error: Chrome failed to start: exited abnormally.\n  (chrome not reachable)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x5cae5a47a133 <unknown>\n#1 0x5cae5a1ae966 <unknown>\n#2 0x5cae5a1d821a <unknown>\n#3 0x5cae5a1d407b <unknown>\n#4 0x5cae5a2139ad <unknown>\n#5 0x5cae5a21318f <unknown>\n#6 0x5cae5a20a9a3 <unknown>\n#7 0x5cae5a1df46a <unknown>\n#8 0x5cae5a1e055e <unknown>\n#9 0x5cae5a439cae <unknown>\n#10 0x5cae5a43d8fe <unknown>\n#11 0x5cae5a446f20 <unknown>\n#12 0x5cae5a43e923 <unknown>\n#13 0x5cae5a411c0e <unknown>\n#14 0x5cae5a461b08 <unknown>\n#15 0x5cae5a461c97 <unknown>\n#16 0x5cae5a472113 <unknown>\n#17 0x7d5e42a95ac3 <unknown>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!chromium-browser --version\n",
        "!chromedriver --version\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NajInK_agqMM",
        "outputId": "196e1bd6-e7d9-4bff-8859-704c759e8334"
      },
      "execution_count": 45,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Command '/usr/bin/chromium-browser' requires the chromium snap to be installed.\n",
            "Please install it with:\n",
            "\n",
            "snap install chromium\n",
            "\n",
            "ChromeDriver 113.0.5672.63 (0e1a4471d5ae5bf128b1bd8f4d627c8cbd55f70c-refs/branch-heads/5672@{#912})\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sudo snap install chromium\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 106
        },
        "id": "bw8fQFGWgvzx",
        "outputId": "8e07224e-d0ca-4fdb-dcc3-112915fea02e"
      },
      "execution_count": 46,
      "outputs": [
        {
          "output_type": "error",
          "ename": "SyntaxError",
          "evalue": "invalid syntax (<ipython-input-46-a67ddb8f26f1>, line 1)",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-46-a67ddb8f26f1>\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    sudo snap install chromium\u001b[0m\n\u001b[0m         ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "exit()"
      ],
      "metadata": {
        "id": "JN3XMMaHg41d"
      },
      "execution_count": 47,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "sudo snap install chromium\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 106
        },
        "id": "vk7zFFClg6wY",
        "outputId": "9e705460-5313-4e43-871b-dd48d1cd32ff"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "error",
          "ename": "SyntaxError",
          "evalue": "invalid syntax (<ipython-input-1-a67ddb8f26f1>, line 1)",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-1-a67ddb8f26f1>\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    sudo snap install chromium\u001b[0m\n\u001b[0m         ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sudo snap install chromium\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 106
        },
        "id": "794gJ-ashA93",
        "outputId": "a9d0b534-da9e-42cb-c7d5-34361d97045d"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "error",
          "ename": "SyntaxError",
          "evalue": "invalid syntax (<ipython-input-2-a67ddb8f26f1>, line 1)",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-2-a67ddb8f26f1>\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    sudo snap install chromium\u001b[0m\n\u001b[0m         ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# نصب Chromium و ChromeDriver در Colab\n",
        "!apt-get update # به روزرسانی منابع\n",
        "!apt-get install -y chromium-chromedriver\n",
        "!cp /usr/lib/chromium-browser/chromedriver /usr/bin\n",
        "\n",
        "# نصب Selenium\n",
        "!pip install selenium\n",
        "\n",
        "# پیکربندی Selenium برای استفاده از Chromium\n",
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from selenium.webdriver.common.by import By\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "\n",
        "chrome_options = Options()\n",
        "chrome_options.add_argument('--headless')  # اجرا بدون رابط گرافیکی\n",
        "chrome_options.add_argument('--no-sandbox')\n",
        "chrome_options.add_argument('--disable-dev-shm-usage')\n",
        "chrome_options.add_argument('--remote-debugging-port=9222')  # برای اجرای بدون خطا در Colab\n",
        "\n",
        "# تعیین مسیر ChromeDriver\n",
        "chrome_driver_path = '/usr/bin/chromedriver'\n",
        "service = Service(chrome_driver_path)\n",
        "\n",
        "# راه‌اندازی WebDriver\n",
        "driver = webdriver.Chrome(service=service, options=chrome_options)\n",
        "\n",
        "# باز کردن سایت و چاپ عنوان صفحه\n",
        "driver.get(\"https://www.google.com\")\n",
        "print(driver.title)\n",
        "\n",
        "# بستن مرورگر\n",
        "driver.quit()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "naRzDvuwhNQ7",
        "outputId": "baf4f90b-95e9-4b55-b53b-6e1db120e16c"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\r0% [Working]\r            \rHit:1 https://cloud.r-project.org/bin/linux/ubuntu jammy-cran40/ InRelease\n",
            "Hit:2 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64  InRelease\n",
            "Hit:3 https://r2u.stat.illinois.edu/ubuntu jammy InRelease\n",
            "Hit:4 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy InRelease\n",
            "Hit:5 https://ppa.launchpadcontent.net/graphics-drivers/ppa/ubuntu jammy InRelease\n",
            "Hit:6 http://security.ubuntu.com/ubuntu jammy-security InRelease\n",
            "Hit:7 https://ppa.launchpadcontent.net/ubuntugis/ppa/ubuntu jammy InRelease\n",
            "Hit:8 http://archive.ubuntu.com/ubuntu jammy InRelease\n",
            "Hit:9 http://archive.ubuntu.com/ubuntu jammy-updates InRelease\n",
            "Hit:10 http://archive.ubuntu.com/ubuntu jammy-backports InRelease\n",
            "Reading package lists... Done\n",
            "W: Skipping acquire of configured file 'main/source/Sources' as repository 'https://r2u.stat.illinois.edu/ubuntu jammy InRelease' does not seem to provide it (sources.list entry misspelt?)\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "chromium-chromedriver is already the newest version (1:85.0.4183.83-0ubuntu2.22.04.1).\n",
            "0 upgraded, 0 newly installed, 0 to remove and 31 not upgraded.\n",
            "cp: '/usr/lib/chromium-browser/chromedriver' and '/usr/bin/chromedriver' are the same file\n",
            "Requirement already satisfied: selenium in /usr/local/lib/python3.11/dist-packages (4.29.0)\n",
            "Requirement already satisfied: urllib3<3,>=1.26 in /usr/local/lib/python3.11/dist-packages (from urllib3[socks]<3,>=1.26->selenium) (2.3.0)\n",
            "Requirement already satisfied: trio~=0.17 in /usr/local/lib/python3.11/dist-packages (from selenium) (0.29.0)\n",
            "Requirement already satisfied: trio-websocket~=0.9 in /usr/local/lib/python3.11/dist-packages (from selenium) (0.12.2)\n",
            "Requirement already satisfied: certifi>=2021.10.8 in /usr/local/lib/python3.11/dist-packages (from selenium) (2025.1.31)\n",
            "Requirement already satisfied: typing_extensions~=4.9 in /usr/local/lib/python3.11/dist-packages (from selenium) (4.12.2)\n",
            "Requirement already satisfied: websocket-client~=1.8 in /usr/local/lib/python3.11/dist-packages (from selenium) (1.8.0)\n",
            "Requirement already satisfied: attrs>=23.2.0 in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (25.1.0)\n",
            "Requirement already satisfied: sortedcontainers in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (2.4.0)\n",
            "Requirement already satisfied: idna in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (3.10)\n",
            "Requirement already satisfied: outcome in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (1.3.0.post0)\n",
            "Requirement already satisfied: sniffio>=1.3.0 in /usr/local/lib/python3.11/dist-packages (from trio~=0.17->selenium) (1.3.1)\n",
            "Requirement already satisfied: wsproto>=0.14 in /usr/local/lib/python3.11/dist-packages (from trio-websocket~=0.9->selenium) (1.2.0)\n",
            "Requirement already satisfied: pysocks!=1.5.7,<2.0,>=1.5.6 in /usr/local/lib/python3.11/dist-packages (from urllib3[socks]<3,>=1.26->selenium) (1.7.1)\n",
            "Requirement already satisfied: h11<1,>=0.9.0 in /usr/local/lib/python3.11/dist-packages (from wsproto>=0.14->trio-websocket~=0.9->selenium) (0.14.0)\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "WebDriverException",
          "evalue": "Message: unknown error: Chrome failed to start: exited abnormally.\n  (chrome not reachable)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x5b06571c7133 <unknown>\n#1 0x5b0656efb966 <unknown>\n#2 0x5b0656f2521a <unknown>\n#3 0x5b0656f2107b <unknown>\n#4 0x5b0656f609ad <unknown>\n#5 0x5b0656f6018f <unknown>\n#6 0x5b0656f579a3 <unknown>\n#7 0x5b0656f2c46a <unknown>\n#8 0x5b0656f2d55e <unknown>\n#9 0x5b0657186cae <unknown>\n#10 0x5b065718a8fe <unknown>\n#11 0x5b0657193f20 <unknown>\n#12 0x5b065718b923 <unknown>\n#13 0x5b065715ec0e <unknown>\n#14 0x5b06571aeb08 <unknown>\n#15 0x5b06571aec97 <unknown>\n#16 0x5b06571bf113 <unknown>\n#17 0x7d5494246ac3 <unknown>\n",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m                        Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-3-a91fa26ae0a8>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     24\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     25\u001b[0m \u001b[0;31m# راه‌اندازی WebDriver\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 26\u001b[0;31m \u001b[0mdriver\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mchrome_options\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     27\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     28\u001b[0m \u001b[0;31m# باز کردن سایت و چاپ عنوان صفحه\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chrome/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     43\u001b[0m         \u001b[0moptions\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0mOptions\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     44\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 45\u001b[0;31m         super().__init__(\n\u001b[0m\u001b[1;32m     46\u001b[0m             \u001b[0mbrowser_name\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mDesiredCapabilities\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCHROME\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"browserName\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     47\u001b[0m             \u001b[0mvendor_prefix\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"goog\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chromium/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, browser_name, vendor_prefix, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     64\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     65\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 66\u001b[0;31m             \u001b[0msuper\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__init__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mexecutor\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     67\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     68\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mquit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, command_executor, keep_alive, file_detector, options, locator_converter, web_element_cls, client_config)\u001b[0m\n\u001b[1;32m    248\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_authenticator_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    249\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_client\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 250\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_session\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    251\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_fedcm\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mFedCM\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    252\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mstart_session\u001b[0;34m(self, capabilities)\u001b[0m\n\u001b[1;32m    340\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    341\u001b[0m         \u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_create_caps\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 342\u001b[0;31m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mCommand\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mNEW_SESSION\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcaps\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    343\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msession_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"sessionId\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    344\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"capabilities\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, driver_command, params)\u001b[0m\n\u001b[1;32m    427\u001b[0m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    428\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 429\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    430\u001b[0m             \u001b[0mresponse\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_unwrap_value\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    431\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/errorhandler.py\u001b[0m in \u001b[0;36mcheck_response\u001b[0;34m(self, response)\u001b[0m\n\u001b[1;32m    230\u001b[0m                 \u001b[0malert_text\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"alert\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"text\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    231\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0malert_text\u001b[0m\u001b[0;34m)\u001b[0m  \u001b[0;31m# type: ignore[call-arg]  # mypy is not smart enough here\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 232\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m: Message: unknown error: Chrome failed to start: exited abnormally.\n  (chrome not reachable)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x5b06571c7133 <unknown>\n#1 0x5b0656efb966 <unknown>\n#2 0x5b0656f2521a <unknown>\n#3 0x5b0656f2107b <unknown>\n#4 0x5b0656f609ad <unknown>\n#5 0x5b0656f6018f <unknown>\n#6 0x5b0656f579a3 <unknown>\n#7 0x5b0656f2c46a <unknown>\n#8 0x5b0656f2d55e <unknown>\n#9 0x5b0657186cae <unknown>\n#10 0x5b065718a8fe <unknown>\n#11 0x5b0657193f20 <unknown>\n#12 0x5b065718b923 <unknown>\n#13 0x5b065715ec0e <unknown>\n#14 0x5b06571aeb08 <unknown>\n#15 0x5b06571aec97 <unknown>\n#16 0x5b06571bf113 <unknown>\n#17 0x7d5494246ac3 <unknown>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "\n",
        "chrome_options = Options()\n",
        "chrome_options.add_argument('--headless')  # اجرا بدون رابط گرافیکی\n",
        "chrome_options.add_argument('--no-sandbox')\n",
        "chrome_options.add_argument('--disable-dev-shm-usage')\n",
        "chrome_options.add_argument('--remote-debugging-port=9222')  # برای اجرای بدون خطا در Colab\n",
        "chrome_options.add_argument('--disable-gpu')  # غیرفعال کردن GPU\n",
        "chrome_options.add_argument('--start-maximized')  # شروع در اندازه کامل\n",
        "\n",
        "# تعیین مسیر ChromeDriver\n",
        "chrome_driver_path = '/usr/bin/chromedriver'\n",
        "service = Service(chrome_driver_path)\n",
        "\n",
        "# راه‌اندازی WebDriver\n",
        "driver = webdriver.Chrome(service=service, options=chrome_options)\n",
        "\n",
        "# باز کردن سایت و چاپ عنوان صفحه\n",
        "driver.get(\"https://www.google.com\")\n",
        "print(driver.title)\n",
        "\n",
        "# بستن مرورگر\n",
        "driver.quit()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 686
        },
        "id": "rkulu2t2hc_H",
        "outputId": "97fe5963-4525-4ab4-b770-d1fb0e766783"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "error",
          "ename": "WebDriverException",
          "evalue": "Message: unknown error: Chrome failed to start: exited abnormally.\n  (chrome not reachable)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x57b13726e133 <unknown>\n#1 0x57b136fa2966 <unknown>\n#2 0x57b136fcc21a <unknown>\n#3 0x57b136fc807b <unknown>\n#4 0x57b1370079ad <unknown>\n#5 0x57b13700718f <unknown>\n#6 0x57b136ffe9a3 <unknown>\n#7 0x57b136fd346a <unknown>\n#8 0x57b136fd455e <unknown>\n#9 0x57b13722dcae <unknown>\n#10 0x57b1372318fe <unknown>\n#11 0x57b13723af20 <unknown>\n#12 0x57b137232923 <unknown>\n#13 0x57b137205c0e <unknown>\n#14 0x57b137255b08 <unknown>\n#15 0x57b137255c97 <unknown>\n#16 0x57b137266113 <unknown>\n#17 0x7db4337acac3 <unknown>\n",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m                        Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-4-3db8affb21f7>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     16\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     17\u001b[0m \u001b[0;31m# راه‌اندازی WebDriver\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 18\u001b[0;31m \u001b[0mdriver\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mchrome_options\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     19\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     20\u001b[0m \u001b[0;31m# باز کردن سایت و چاپ عنوان صفحه\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chrome/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     43\u001b[0m         \u001b[0moptions\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0mOptions\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     44\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 45\u001b[0;31m         super().__init__(\n\u001b[0m\u001b[1;32m     46\u001b[0m             \u001b[0mbrowser_name\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mDesiredCapabilities\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCHROME\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"browserName\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     47\u001b[0m             \u001b[0mvendor_prefix\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"goog\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chromium/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, browser_name, vendor_prefix, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     64\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     65\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 66\u001b[0;31m             \u001b[0msuper\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__init__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mexecutor\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     67\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     68\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mquit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, command_executor, keep_alive, file_detector, options, locator_converter, web_element_cls, client_config)\u001b[0m\n\u001b[1;32m    248\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_authenticator_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    249\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_client\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 250\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_session\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    251\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_fedcm\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mFedCM\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    252\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mstart_session\u001b[0;34m(self, capabilities)\u001b[0m\n\u001b[1;32m    340\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    341\u001b[0m         \u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_create_caps\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 342\u001b[0;31m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mCommand\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mNEW_SESSION\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcaps\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    343\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msession_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"sessionId\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    344\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"capabilities\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, driver_command, params)\u001b[0m\n\u001b[1;32m    427\u001b[0m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    428\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 429\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    430\u001b[0m             \u001b[0mresponse\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_unwrap_value\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    431\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/errorhandler.py\u001b[0m in \u001b[0;36mcheck_response\u001b[0;34m(self, response)\u001b[0m\n\u001b[1;32m    230\u001b[0m                 \u001b[0malert_text\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"alert\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"text\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    231\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0malert_text\u001b[0m\u001b[0;34m)\u001b[0m  \u001b[0;31m# type: ignore[call-arg]  # mypy is not smart enough here\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 232\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m: Message: unknown error: Chrome failed to start: exited abnormally.\n  (chrome not reachable)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x57b13726e133 <unknown>\n#1 0x57b136fa2966 <unknown>\n#2 0x57b136fcc21a <unknown>\n#3 0x57b136fc807b <unknown>\n#4 0x57b1370079ad <unknown>\n#5 0x57b13700718f <unknown>\n#6 0x57b136ffe9a3 <unknown>\n#7 0x57b136fd346a <unknown>\n#8 0x57b136fd455e <unknown>\n#9 0x57b13722dcae <unknown>\n#10 0x57b1372318fe <unknown>\n#11 0x57b13723af20 <unknown>\n#12 0x57b137232923 <unknown>\n#13 0x57b137205c0e <unknown>\n#14 0x57b137255b08 <unknown>\n#15 0x57b137255c97 <unknown>\n#16 0x57b137266113 <unknown>\n#17 0x7db4337acac3 <unknown>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!apt-get update\n",
        "!apt-get install -y chromium-browser=114.0.5735.90-1\n",
        "!apt-get install -y chromium-chromedriver=114.0.5735.90-1\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "V-722oKfhisw",
        "outputId": "7e92dc45-21ac-4eb4-ec65-3eb24252dc63"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\r0% [Working]\r            \rHit:1 http://security.ubuntu.com/ubuntu jammy-security InRelease\n",
            "\r0% [Connecting to archive.ubuntu.com] [Connected to cloud.r-project.org (18.160.213.79)] [Connected \r                                                                                                    \rHit:2 https://cloud.r-project.org/bin/linux/ubuntu jammy-cran40/ InRelease\n",
            "\r0% [Connecting to archive.ubuntu.com (185.125.190.82)] [Waiting for headers] [Waiting for headers] [\r                                                                                                    \rHit:3 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64  InRelease\n",
            "Hit:4 https://r2u.stat.illinois.edu/ubuntu jammy InRelease\n",
            "Hit:5 http://archive.ubuntu.com/ubuntu jammy InRelease\n",
            "Hit:6 http://archive.ubuntu.com/ubuntu jammy-updates InRelease\n",
            "Hit:7 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy InRelease\n",
            "Hit:8 http://archive.ubuntu.com/ubuntu jammy-backports InRelease\n",
            "Hit:9 https://ppa.launchpadcontent.net/graphics-drivers/ppa/ubuntu jammy InRelease\n",
            "Hit:10 https://ppa.launchpadcontent.net/ubuntugis/ppa/ubuntu jammy InRelease\n",
            "Reading package lists... Done\n",
            "W: Skipping acquire of configured file 'main/source/Sources' as repository 'https://r2u.stat.illinois.edu/ubuntu jammy InRelease' does not seem to provide it (sources.list entry misspelt?)\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "Package chromium-browser is not available, but is referred to by another package.\n",
            "This may mean that the package is missing, has been obsoleted, or\n",
            "is only available from another source\n",
            "\n",
            "E: Version '114.0.5735.90-1' for 'chromium-browser' was not found\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "Package chromium-chromedriver is not available, but is referred to by another package.\n",
            "This may mean that the package is missing, has been obsoleted, or\n",
            "is only available from another source\n",
            "\n",
            "E: Version '114.0.5735.90-1' for 'chromium-chromedriver' was not found\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "chrome_options.add_argument('--binary=/usr/bin/chromium-browser')\n"
      ],
      "metadata": {
        "id": "-fKoG6uVhmQl"
      },
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "\n",
        "# پیکربندی ChromeOptions\n",
        "chrome_options = Options()\n",
        "chrome_options.add_argument('--headless')  # اجرا بدون رابط گرافیکی\n",
        "chrome_options.add_argument('--no-sandbox')\n",
        "chrome_options.add_argument('--disable-dev-shm-usage')\n",
        "chrome_options.add_argument('--remote-debugging-port=9222')  # برای اجرای بدون خطا در Colab\n",
        "chrome_options.add_argument('--disable-gpu')  # غیرفعال کردن GPU\n",
        "chrome_options.add_argument('--start-maximized')  # شروع در اندازه کامل\n",
        "chrome_options.add_argument('--binary=/usr/bin/chromium-browser')  # مسیر دقیق Chromium\n",
        "\n",
        "# تعیین مسیر ChromeDriver\n",
        "chrome_driver_path = '/usr/bin/chromedriver'\n",
        "service = Service(chrome_driver_path)\n",
        "\n",
        "# راه‌اندازی WebDriver\n",
        "driver = webdriver.Chrome(service=service, options=chrome_options)\n",
        "\n",
        "# باز کردن سایت و چاپ عنوان صفحه\n",
        "driver.get(\"https://www.google.com\")\n",
        "print(driver.title)\n",
        "\n",
        "# بستن مرورگر\n",
        "driver.quit()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 686
        },
        "id": "OEZrTkPZhobz",
        "outputId": "aa098c08-8896-46d3-a9a9-8de8acdfb42e"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "error",
          "ename": "WebDriverException",
          "evalue": "Message: unknown error: Chrome failed to start: exited abnormally.\n  (chrome not reachable)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x5568c57dd133 <unknown>\n#1 0x5568c5511966 <unknown>\n#2 0x5568c553b21a <unknown>\n#3 0x5568c553707b <unknown>\n#4 0x5568c55769ad <unknown>\n#5 0x5568c557618f <unknown>\n#6 0x5568c556d9a3 <unknown>\n#7 0x5568c554246a <unknown>\n#8 0x5568c554355e <unknown>\n#9 0x5568c579ccae <unknown>\n#10 0x5568c57a08fe <unknown>\n#11 0x5568c57a9f20 <unknown>\n#12 0x5568c57a1923 <unknown>\n#13 0x5568c5774c0e <unknown>\n#14 0x5568c57c4b08 <unknown>\n#15 0x5568c57c4c97 <unknown>\n#16 0x5568c57d5113 <unknown>\n#17 0x7ec0522bfac3 <unknown>\n",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m                        Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-7-a4024337e291>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     18\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     19\u001b[0m \u001b[0;31m# راه‌اندازی WebDriver\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 20\u001b[0;31m \u001b[0mdriver\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mchrome_options\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     21\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     22\u001b[0m \u001b[0;31m# باز کردن سایت و چاپ عنوان صفحه\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chrome/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     43\u001b[0m         \u001b[0moptions\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0mOptions\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     44\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 45\u001b[0;31m         super().__init__(\n\u001b[0m\u001b[1;32m     46\u001b[0m             \u001b[0mbrowser_name\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mDesiredCapabilities\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCHROME\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"browserName\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     47\u001b[0m             \u001b[0mvendor_prefix\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"goog\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chromium/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, browser_name, vendor_prefix, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     64\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     65\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 66\u001b[0;31m             \u001b[0msuper\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__init__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mexecutor\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     67\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     68\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mquit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, command_executor, keep_alive, file_detector, options, locator_converter, web_element_cls, client_config)\u001b[0m\n\u001b[1;32m    248\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_authenticator_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    249\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_client\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 250\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_session\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    251\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_fedcm\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mFedCM\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    252\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mstart_session\u001b[0;34m(self, capabilities)\u001b[0m\n\u001b[1;32m    340\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    341\u001b[0m         \u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_create_caps\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 342\u001b[0;31m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mCommand\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mNEW_SESSION\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcaps\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    343\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msession_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"sessionId\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    344\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"capabilities\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, driver_command, params)\u001b[0m\n\u001b[1;32m    427\u001b[0m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    428\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 429\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    430\u001b[0m             \u001b[0mresponse\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_unwrap_value\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    431\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/errorhandler.py\u001b[0m in \u001b[0;36mcheck_response\u001b[0;34m(self, response)\u001b[0m\n\u001b[1;32m    230\u001b[0m                 \u001b[0malert_text\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"alert\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"text\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    231\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0malert_text\u001b[0m\u001b[0;34m)\u001b[0m  \u001b[0;31m# type: ignore[call-arg]  # mypy is not smart enough here\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 232\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m: Message: unknown error: Chrome failed to start: exited abnormally.\n  (chrome not reachable)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x5568c57dd133 <unknown>\n#1 0x5568c5511966 <unknown>\n#2 0x5568c553b21a <unknown>\n#3 0x5568c553707b <unknown>\n#4 0x5568c55769ad <unknown>\n#5 0x5568c557618f <unknown>\n#6 0x5568c556d9a3 <unknown>\n#7 0x5568c554246a <unknown>\n#8 0x5568c554355e <unknown>\n#9 0x5568c579ccae <unknown>\n#10 0x5568c57a08fe <unknown>\n#11 0x5568c57a9f20 <unknown>\n#12 0x5568c57a1923 <unknown>\n#13 0x5568c5774c0e <unknown>\n#14 0x5568c57c4b08 <unknown>\n#15 0x5568c57c4c97 <unknown>\n#16 0x5568c57d5113 <unknown>\n#17 0x7ec0522bfac3 <unknown>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!apt-get update\n",
        "!apt-get install -y chromium-browser=114.0.5735.90-1\n",
        "!apt-get install -y chromium-chromedriver=114.0.5735.90-1\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0UECAdbZhui2",
        "outputId": "c690781d-6827-47eb-c793-45ee0332d0f1"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\r0% [Working]\r            \rHit:1 https://cloud.r-project.org/bin/linux/ubuntu jammy-cran40/ InRelease\n",
            "\r0% [Waiting for headers] [Waiting for headers] [Waiting for headers] [Waiting for headers] [Connecte\r                                                                                                    \rHit:2 http://archive.ubuntu.com/ubuntu jammy InRelease\n",
            "\r0% [Waiting for headers] [Waiting for headers] [Waiting for headers] [Waiting for headers] [Connecte\r                                                                                                    \rHit:3 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64  InRelease\n",
            "Hit:4 http://archive.ubuntu.com/ubuntu jammy-updates InRelease\n",
            "Hit:5 https://r2u.stat.illinois.edu/ubuntu jammy InRelease\n",
            "Hit:6 http://archive.ubuntu.com/ubuntu jammy-backports InRelease\n",
            "Hit:7 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy InRelease\n",
            "Hit:8 https://ppa.launchpadcontent.net/graphics-drivers/ppa/ubuntu jammy InRelease\n",
            "Hit:9 https://ppa.launchpadcontent.net/ubuntugis/ppa/ubuntu jammy InRelease\n",
            "Hit:10 http://security.ubuntu.com/ubuntu jammy-security InRelease\n",
            "Reading package lists... Done\n",
            "W: Skipping acquire of configured file 'main/source/Sources' as repository 'https://r2u.stat.illinois.edu/ubuntu jammy InRelease' does not seem to provide it (sources.list entry misspelt?)\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "Package chromium-browser is not available, but is referred to by another package.\n",
            "This may mean that the package is missing, has been obsoleted, or\n",
            "is only available from another source\n",
            "\n",
            "E: Version '114.0.5735.90-1' for 'chromium-browser' was not found\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "Package chromium-chromedriver is not available, but is referred to by another package.\n",
            "This may mean that the package is missing, has been obsoleted, or\n",
            "is only available from another source\n",
            "\n",
            "E: Version '114.0.5735.90-1' for 'chromium-chromedriver' was not found\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "\n",
        "# پیکربندی ChromeOptions\n",
        "chrome_options = Options()\n",
        "chrome_options.add_argument('--headless')  # اجرا بدون رابط گرافیکی\n",
        "chrome_options.add_argument('--no-sandbox')\n",
        "chrome_options.add_argument('--disable-dev-shm-usage')\n",
        "chrome_options.add_argument('--remote-debugging-port=9222')  # برای اجرای بدون خطا در Colab\n",
        "chrome_options.add_argument('--disable-gpu')  # غیرفعال کردن GPU\n",
        "chrome_options.add_argument('--start-maximized')  # شروع در اندازه کامل\n",
        "chrome_options.add_argument('--binary=/usr/bin/chromium-browser')  # مسیر دقیق Chromium\n",
        "\n",
        "# تعیین مسیر ChromeDriver\n",
        "chrome_driver_path = '/usr/bin/chromedriver'\n",
        "service = Service(chrome_driver_path)\n",
        "\n",
        "# راه‌اندازی WebDriver\n",
        "driver = webdriver.Chrome(service=service, options=chrome_options)\n",
        "\n",
        "# باز کردن سایت و چاپ عنوان صفحه\n",
        "driver.get(\"https://www.google.com\")\n",
        "print(driver.title)\n",
        "\n",
        "# بستن مرورگر\n",
        "driver.quit()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 686
        },
        "id": "kxRQ3Iu_hzGp",
        "outputId": "4ef0eb33-38a9-4405-fbce-d3c222f5bb56"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "error",
          "ename": "WebDriverException",
          "evalue": "Message: unknown error: Chrome failed to start: exited abnormally.\n  (chrome not reachable)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x58077e3cd133 <unknown>\n#1 0x58077e101966 <unknown>\n#2 0x58077e12b21a <unknown>\n#3 0x58077e12707b <unknown>\n#4 0x58077e1669ad <unknown>\n#5 0x58077e16618f <unknown>\n#6 0x58077e15d9a3 <unknown>\n#7 0x58077e13246a <unknown>\n#8 0x58077e13355e <unknown>\n#9 0x58077e38ccae <unknown>\n#10 0x58077e3908fe <unknown>\n#11 0x58077e399f20 <unknown>\n#12 0x58077e391923 <unknown>\n#13 0x58077e364c0e <unknown>\n#14 0x58077e3b4b08 <unknown>\n#15 0x58077e3b4c97 <unknown>\n#16 0x58077e3c5113 <unknown>\n#17 0x7baddcca1ac3 <unknown>\n",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m                        Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-9-a4024337e291>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     18\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     19\u001b[0m \u001b[0;31m# راه‌اندازی WebDriver\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 20\u001b[0;31m \u001b[0mdriver\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mchrome_options\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     21\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     22\u001b[0m \u001b[0;31m# باز کردن سایت و چاپ عنوان صفحه\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chrome/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     43\u001b[0m         \u001b[0moptions\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0mOptions\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     44\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 45\u001b[0;31m         super().__init__(\n\u001b[0m\u001b[1;32m     46\u001b[0m             \u001b[0mbrowser_name\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mDesiredCapabilities\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCHROME\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"browserName\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     47\u001b[0m             \u001b[0mvendor_prefix\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"goog\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chromium/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, browser_name, vendor_prefix, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     64\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     65\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 66\u001b[0;31m             \u001b[0msuper\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__init__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mexecutor\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     67\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     68\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mquit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, command_executor, keep_alive, file_detector, options, locator_converter, web_element_cls, client_config)\u001b[0m\n\u001b[1;32m    248\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_authenticator_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    249\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_client\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 250\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_session\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    251\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_fedcm\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mFedCM\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    252\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mstart_session\u001b[0;34m(self, capabilities)\u001b[0m\n\u001b[1;32m    340\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    341\u001b[0m         \u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_create_caps\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 342\u001b[0;31m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mCommand\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mNEW_SESSION\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcaps\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    343\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msession_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"sessionId\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    344\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"capabilities\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, driver_command, params)\u001b[0m\n\u001b[1;32m    427\u001b[0m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    428\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 429\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    430\u001b[0m             \u001b[0mresponse\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_unwrap_value\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    431\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/errorhandler.py\u001b[0m in \u001b[0;36mcheck_response\u001b[0;34m(self, response)\u001b[0m\n\u001b[1;32m    230\u001b[0m                 \u001b[0malert_text\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"alert\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"text\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    231\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0malert_text\u001b[0m\u001b[0;34m)\u001b[0m  \u001b[0;31m# type: ignore[call-arg]  # mypy is not smart enough here\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 232\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m: Message: unknown error: Chrome failed to start: exited abnormally.\n  (chrome not reachable)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x58077e3cd133 <unknown>\n#1 0x58077e101966 <unknown>\n#2 0x58077e12b21a <unknown>\n#3 0x58077e12707b <unknown>\n#4 0x58077e1669ad <unknown>\n#5 0x58077e16618f <unknown>\n#6 0x58077e15d9a3 <unknown>\n#7 0x58077e13246a <unknown>\n#8 0x58077e13355e <unknown>\n#9 0x58077e38ccae <unknown>\n#10 0x58077e3908fe <unknown>\n#11 0x58077e399f20 <unknown>\n#12 0x58077e391923 <unknown>\n#13 0x58077e364c0e <unknown>\n#14 0x58077e3b4b08 <unknown>\n#15 0x58077e3b4c97 <unknown>\n#16 0x58077e3c5113 <unknown>\n#17 0x7baddcca1ac3 <unknown>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "chrome_options.add_argument('--disable-software-rasterizer')\n",
        "chrome_options.add_argument('--disable-extensions')\n",
        "chrome_options.add_argument('--disable-plugins')\n",
        "chrome_options.add_argument('--disable-translate')\n"
      ],
      "metadata": {
        "id": "YbQUp30Jh4vJ"
      },
      "execution_count": 10,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "\n",
        "# پیکربندی ChromeOptions\n",
        "chrome_options = Options()\n",
        "chrome_options.add_argument('--headless')  # اجرا بدون رابط گرافیکی\n",
        "chrome_options.add_argument('--no-sandbox')\n",
        "chrome_options.add_argument('--disable-dev-shm-usage')\n",
        "chrome_options.add_argument('--remote-debugging-port=9222')  # برای اجرای بدون خطا در Colab\n",
        "chrome_options.add_argument('--disable-gpu')  # غیرفعال کردن GPU\n",
        "chrome_options.add_argument('--start-maximized')  # شروع در اندازه کامل\n",
        "chrome_options.add_argument('--binary=/usr/bin/chromium-browser')  # مسیر دقیق Chromium\n",
        "\n",
        "# تعیین مسیر ChromeDriver\n",
        "chrome_driver_path = '/usr/bin/chromedriver'\n",
        "service = Service(chrome_driver_path)\n",
        "\n",
        "# راه‌اندازی WebDriver\n",
        "driver = webdriver.Chrome(service=service, options=chrome_options)\n",
        "\n",
        "# باز کردن سایت و چاپ عنوان صفحه\n",
        "driver.get(\"https://www.google.com\")\n",
        "print(driver.title)\n",
        "\n",
        "# بستن مرورگر\n",
        "driver.quit()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 686
        },
        "id": "ruuKmE-Gh7CO",
        "outputId": "e069a10f-aab1-4405-97bf-5e07ccee1638"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "error",
          "ename": "WebDriverException",
          "evalue": "Message: unknown error: Chrome failed to start: exited abnormally.\n  (chrome not reachable)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x590ac93ea133 <unknown>\n#1 0x590ac911e966 <unknown>\n#2 0x590ac914821a <unknown>\n#3 0x590ac914407b <unknown>\n#4 0x590ac91839ad <unknown>\n#5 0x590ac918318f <unknown>\n#6 0x590ac917a9a3 <unknown>\n#7 0x590ac914f46a <unknown>\n#8 0x590ac915055e <unknown>\n#9 0x590ac93a9cae <unknown>\n#10 0x590ac93ad8fe <unknown>\n#11 0x590ac93b6f20 <unknown>\n#12 0x590ac93ae923 <unknown>\n#13 0x590ac9381c0e <unknown>\n#14 0x590ac93d1b08 <unknown>\n#15 0x590ac93d1c97 <unknown>\n#16 0x590ac93e2113 <unknown>\n#17 0x7bdc1d810ac3 <unknown>\n",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m                        Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-11-a4024337e291>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     18\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     19\u001b[0m \u001b[0;31m# راه‌اندازی WebDriver\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 20\u001b[0;31m \u001b[0mdriver\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mchrome_options\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     21\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     22\u001b[0m \u001b[0;31m# باز کردن سایت و چاپ عنوان صفحه\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chrome/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     43\u001b[0m         \u001b[0moptions\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0mOptions\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     44\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 45\u001b[0;31m         super().__init__(\n\u001b[0m\u001b[1;32m     46\u001b[0m             \u001b[0mbrowser_name\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mDesiredCapabilities\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCHROME\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"browserName\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     47\u001b[0m             \u001b[0mvendor_prefix\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"goog\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chromium/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, browser_name, vendor_prefix, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     64\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     65\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 66\u001b[0;31m             \u001b[0msuper\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__init__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mexecutor\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     67\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     68\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mquit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, command_executor, keep_alive, file_detector, options, locator_converter, web_element_cls, client_config)\u001b[0m\n\u001b[1;32m    248\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_authenticator_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    249\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_client\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 250\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_session\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    251\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_fedcm\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mFedCM\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    252\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mstart_session\u001b[0;34m(self, capabilities)\u001b[0m\n\u001b[1;32m    340\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    341\u001b[0m         \u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_create_caps\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 342\u001b[0;31m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mCommand\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mNEW_SESSION\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcaps\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    343\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msession_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"sessionId\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    344\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"capabilities\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, driver_command, params)\u001b[0m\n\u001b[1;32m    427\u001b[0m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    428\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 429\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    430\u001b[0m             \u001b[0mresponse\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_unwrap_value\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    431\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/errorhandler.py\u001b[0m in \u001b[0;36mcheck_response\u001b[0;34m(self, response)\u001b[0m\n\u001b[1;32m    230\u001b[0m                 \u001b[0malert_text\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"alert\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"text\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    231\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0malert_text\u001b[0m\u001b[0;34m)\u001b[0m  \u001b[0;31m# type: ignore[call-arg]  # mypy is not smart enough here\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 232\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m: Message: unknown error: Chrome failed to start: exited abnormally.\n  (chrome not reachable)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x590ac93ea133 <unknown>\n#1 0x590ac911e966 <unknown>\n#2 0x590ac914821a <unknown>\n#3 0x590ac914407b <unknown>\n#4 0x590ac91839ad <unknown>\n#5 0x590ac918318f <unknown>\n#6 0x590ac917a9a3 <unknown>\n#7 0x590ac914f46a <unknown>\n#8 0x590ac915055e <unknown>\n#9 0x590ac93a9cae <unknown>\n#10 0x590ac93ad8fe <unknown>\n#11 0x590ac93b6f20 <unknown>\n#12 0x590ac93ae923 <unknown>\n#13 0x590ac9381c0e <unknown>\n#14 0x590ac93d1b08 <unknown>\n#15 0x590ac93d1c97 <unknown>\n#16 0x590ac93e2113 <unknown>\n#17 0x7bdc1d810ac3 <unknown>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!apt-get update\n",
        "!apt-get install -y chromium-browser\n",
        "!apt-get install -y chromium-chromedriver\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YVgGAIv-iCPW",
        "outputId": "b179f163-df81-4a72-9b2e-872263022110"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\r0% [Working]\r            \rHit:1 https://cloud.r-project.org/bin/linux/ubuntu jammy-cran40/ InRelease\n",
            "\r0% [Connecting to archive.ubuntu.com (185.125.190.83)] [Waiting for headers] [Waiting for headers] [\r                                                                                                    \rHit:2 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64  InRelease\n",
            "Hit:3 https://r2u.stat.illinois.edu/ubuntu jammy InRelease\n",
            "Hit:4 http://security.ubuntu.com/ubuntu jammy-security InRelease\n",
            "Hit:5 http://archive.ubuntu.com/ubuntu jammy InRelease\n",
            "Hit:6 http://archive.ubuntu.com/ubuntu jammy-updates InRelease\n",
            "Hit:7 http://archive.ubuntu.com/ubuntu jammy-backports InRelease\n",
            "Hit:8 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy InRelease\n",
            "Hit:9 https://ppa.launchpadcontent.net/graphics-drivers/ppa/ubuntu jammy InRelease\n",
            "Hit:10 https://ppa.launchpadcontent.net/ubuntugis/ppa/ubuntu jammy InRelease\n",
            "Reading package lists... Done\n",
            "W: Skipping acquire of configured file 'main/source/Sources' as repository 'https://r2u.stat.illinois.edu/ubuntu jammy InRelease' does not seem to provide it (sources.list entry misspelt?)\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "chromium-browser is already the newest version (1:85.0.4183.83-0ubuntu2.22.04.1).\n",
            "0 upgraded, 0 newly installed, 0 to remove and 31 not upgraded.\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "chromium-chromedriver is already the newest version (1:85.0.4183.83-0ubuntu2.22.04.1).\n",
            "0 upgraded, 0 newly installed, 0 to remove and 31 not upgraded.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "\n",
        "# پیکربندی ChromeOptions\n",
        "chrome_options = Options()\n",
        "chrome_options.add_argument('--headless')  # اجرا بدون رابط گرافیکی\n",
        "chrome_options.add_argument('--no-sandbox')\n",
        "chrome_options.add_argument('--disable-dev-shm-usage')\n",
        "chrome_options.add_argument('--remote-debugging-port=9222')  # برای اجرای بدون خطا در Colab\n",
        "chrome_options.add_argument('--disable-gpu')  # غیرفعال کردن GPU\n",
        "chrome_options.add_argument('--start-maximized')  # شروع در اندازه کامل\n",
        "chrome_options.add_argument('--binary=/usr/bin/chromium-browser')  # مسیر دقیق Chromium\n",
        "\n",
        "# افزودن گزینه‌های بیشتر برای جلوگیری از مشکلات بارگذاری منابع\n",
        "chrome_options.add_argument('--disable-software-rasterizer')\n",
        "chrome_options.add_argument('--disable-extensions')\n",
        "chrome_options.add_argument('--disable-plugins')\n",
        "chrome_options.add_argument('--disable-translate')\n",
        "\n",
        "# تعیین مسیر ChromeDriver\n",
        "chrome_driver_path = '/usr/bin/chromedriver'\n",
        "service = Service(chrome_driver_path)\n",
        "\n",
        "# راه‌اندازی WebDriver\n",
        "driver = webdriver.Chrome(service=service, options=chrome_options)\n",
        "\n",
        "# باز کردن سایت و چاپ عنوان صفحه\n",
        "driver.get(\"https://www.google.com\")\n",
        "print(driver.title)\n",
        "\n",
        "# بستن مرورگر\n",
        "driver.quit()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 686
        },
        "id": "qLmtGr3WiGpt",
        "outputId": "c0d9b49c-38a5-4951-d49f-14d81e12b246"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "error",
          "ename": "WebDriverException",
          "evalue": "Message: unknown error: Chrome failed to start: exited abnormally.\n  (chrome not reachable)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x59b1581d7133 <unknown>\n#1 0x59b157f0b966 <unknown>\n#2 0x59b157f3521a <unknown>\n#3 0x59b157f3107b <unknown>\n#4 0x59b157f709ad <unknown>\n#5 0x59b157f7018f <unknown>\n#6 0x59b157f679a3 <unknown>\n#7 0x59b157f3c46a <unknown>\n#8 0x59b157f3d55e <unknown>\n#9 0x59b158196cae <unknown>\n#10 0x59b15819a8fe <unknown>\n#11 0x59b1581a3f20 <unknown>\n#12 0x59b15819b923 <unknown>\n#13 0x59b15816ec0e <unknown>\n#14 0x59b1581beb08 <unknown>\n#15 0x59b1581bec97 <unknown>\n#16 0x59b1581cf113 <unknown>\n#17 0x7de3036ecac3 <unknown>\n",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m                        Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-13-00ccc0f0b1d7>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     24\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     25\u001b[0m \u001b[0;31m# راه‌اندازی WebDriver\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 26\u001b[0;31m \u001b[0mdriver\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mchrome_options\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     27\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     28\u001b[0m \u001b[0;31m# باز کردن سایت و چاپ عنوان صفحه\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chrome/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     43\u001b[0m         \u001b[0moptions\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0mOptions\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     44\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 45\u001b[0;31m         super().__init__(\n\u001b[0m\u001b[1;32m     46\u001b[0m             \u001b[0mbrowser_name\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mDesiredCapabilities\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCHROME\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"browserName\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     47\u001b[0m             \u001b[0mvendor_prefix\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"goog\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chromium/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, browser_name, vendor_prefix, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     64\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     65\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 66\u001b[0;31m             \u001b[0msuper\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__init__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mexecutor\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     67\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     68\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mquit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, command_executor, keep_alive, file_detector, options, locator_converter, web_element_cls, client_config)\u001b[0m\n\u001b[1;32m    248\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_authenticator_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    249\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_client\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 250\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_session\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    251\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_fedcm\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mFedCM\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    252\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mstart_session\u001b[0;34m(self, capabilities)\u001b[0m\n\u001b[1;32m    340\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    341\u001b[0m         \u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_create_caps\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 342\u001b[0;31m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mCommand\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mNEW_SESSION\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcaps\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    343\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msession_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"sessionId\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    344\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"capabilities\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, driver_command, params)\u001b[0m\n\u001b[1;32m    427\u001b[0m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    428\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 429\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    430\u001b[0m             \u001b[0mresponse\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_unwrap_value\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    431\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/errorhandler.py\u001b[0m in \u001b[0;36mcheck_response\u001b[0;34m(self, response)\u001b[0m\n\u001b[1;32m    230\u001b[0m                 \u001b[0malert_text\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"alert\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"text\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    231\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0malert_text\u001b[0m\u001b[0;34m)\u001b[0m  \u001b[0;31m# type: ignore[call-arg]  # mypy is not smart enough here\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 232\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m: Message: unknown error: Chrome failed to start: exited abnormally.\n  (chrome not reachable)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x59b1581d7133 <unknown>\n#1 0x59b157f0b966 <unknown>\n#2 0x59b157f3521a <unknown>\n#3 0x59b157f3107b <unknown>\n#4 0x59b157f709ad <unknown>\n#5 0x59b157f7018f <unknown>\n#6 0x59b157f679a3 <unknown>\n#7 0x59b157f3c46a <unknown>\n#8 0x59b157f3d55e <unknown>\n#9 0x59b158196cae <unknown>\n#10 0x59b15819a8fe <unknown>\n#11 0x59b1581a3f20 <unknown>\n#12 0x59b15819b923 <unknown>\n#13 0x59b15816ec0e <unknown>\n#14 0x59b1581beb08 <unknown>\n#15 0x59b1581bec97 <unknown>\n#16 0x59b1581cf113 <unknown>\n#17 0x7de3036ecac3 <unknown>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "--disable-dev-shm-usage"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 141
        },
        "id": "Tca0z6RgiJ6K",
        "outputId": "4f61cb05-3ddc-4944-aa7e-72bc32d4737f"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "name 'disable' is not defined",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-14-c77d9df7c873>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;34m-\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0mdisable\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0mdev\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0mshm\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0musage\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m: name 'disable' is not defined"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from selenium import webdriver\n",
        "from selenium.webdriver.chrome.service import Service\n",
        "from selenium.webdriver.chrome.options import Options\n",
        "\n",
        "# پیکربندی ChromeOptions\n",
        "chrome_options = Options()\n",
        "chrome_options.add_argument('--headless')  # اجرا بدون رابط گرافیکی\n",
        "chrome_options.add_argument('--no-sandbox')\n",
        "chrome_options.add_argument('--disable-dev-shm-usage')  # افزودن این گزینه\n",
        "chrome_options.add_argument('--remote-debugging-port=9222')  # برای اجرای بدون خطا در Colab\n",
        "chrome_options.add_argument('--disable-gpu')  # غیرفعال کردن GPU\n",
        "chrome_options.add_argument('--start-maximized')  # شروع در اندازه کامل\n",
        "chrome_options.add_argument('--binary=/usr/bin/chromium-browser')  # مسیر دقیق Chromium\n",
        "\n",
        "# تعیین مسیر ChromeDriver\n",
        "chrome_driver_path = '/usr/bin/chromedriver'\n",
        "service = Service(chrome_driver_path)\n",
        "\n",
        "# راه‌اندازی WebDriver\n",
        "driver = webdriver.Chrome(service=service, options=chrome_options)\n",
        "\n",
        "# باز کردن سایت و چاپ عنوان صفحه\n",
        "driver.get(\"https://www.google.com\")\n",
        "print(driver.title)\n",
        "\n",
        "# بستن مرورگر\n",
        "driver.quit()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 686
        },
        "id": "-QEC2uBwiPTx",
        "outputId": "057f6c7c-650d-4a5c-ff05-05e706110b6b"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "error",
          "ename": "WebDriverException",
          "evalue": "Message: unknown error: Chrome failed to start: exited abnormally.\n  (chrome not reachable)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x5a8f4f26d133 <unknown>\n#1 0x5a8f4efa1966 <unknown>\n#2 0x5a8f4efcb21a <unknown>\n#3 0x5a8f4efc707b <unknown>\n#4 0x5a8f4f0069ad <unknown>\n#5 0x5a8f4f00618f <unknown>\n#6 0x5a8f4effd9a3 <unknown>\n#7 0x5a8f4efd246a <unknown>\n#8 0x5a8f4efd355e <unknown>\n#9 0x5a8f4f22ccae <unknown>\n#10 0x5a8f4f2308fe <unknown>\n#11 0x5a8f4f239f20 <unknown>\n#12 0x5a8f4f231923 <unknown>\n#13 0x5a8f4f204c0e <unknown>\n#14 0x5a8f4f254b08 <unknown>\n#15 0x5a8f4f254c97 <unknown>\n#16 0x5a8f4f265113 <unknown>\n#17 0x796c46040ac3 <unknown>\n",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m                        Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-15-e9dfc4e5fe45>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     18\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     19\u001b[0m \u001b[0;31m# راه‌اندازی WebDriver\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 20\u001b[0;31m \u001b[0mdriver\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mchrome_options\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     21\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     22\u001b[0m \u001b[0;31m# باز کردن سایت و چاپ عنوان صفحه\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chrome/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     43\u001b[0m         \u001b[0moptions\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0moptions\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0mOptions\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     44\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 45\u001b[0;31m         super().__init__(\n\u001b[0m\u001b[1;32m     46\u001b[0m             \u001b[0mbrowser_name\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mDesiredCapabilities\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCHROME\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"browserName\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     47\u001b[0m             \u001b[0mvendor_prefix\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"goog\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/chromium/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, browser_name, vendor_prefix, options, service, keep_alive)\u001b[0m\n\u001b[1;32m     64\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     65\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 66\u001b[0;31m             \u001b[0msuper\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__init__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mexecutor\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     67\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     68\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mquit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, command_executor, keep_alive, file_detector, options, locator_converter, web_element_cls, client_config)\u001b[0m\n\u001b[1;32m    248\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_authenticator_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    249\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_client\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 250\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_session\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    251\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_fedcm\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mFedCM\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    252\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mstart_session\u001b[0;34m(self, capabilities)\u001b[0m\n\u001b[1;32m    340\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    341\u001b[0m         \u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_create_caps\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 342\u001b[0;31m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mCommand\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mNEW_SESSION\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcaps\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    343\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msession_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"sessionId\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    344\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcaps\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"capabilities\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, driver_command, params)\u001b[0m\n\u001b[1;32m    427\u001b[0m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    428\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 429\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    430\u001b[0m             \u001b[0mresponse\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_unwrap_value\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"value\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    431\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/selenium/webdriver/remote/errorhandler.py\u001b[0m in \u001b[0;36mcheck_response\u001b[0;34m(self, response)\u001b[0m\n\u001b[1;32m    230\u001b[0m                 \u001b[0malert_text\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"alert\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"text\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    231\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0malert_text\u001b[0m\u001b[0;34m)\u001b[0m  \u001b[0;31m# type: ignore[call-arg]  # mypy is not smart enough here\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 232\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mWebDriverException\u001b[0m: Message: unknown error: Chrome failed to start: exited abnormally.\n  (chrome not reachable)\n  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)\nStacktrace:\n#0 0x5a8f4f26d133 <unknown>\n#1 0x5a8f4efa1966 <unknown>\n#2 0x5a8f4efcb21a <unknown>\n#3 0x5a8f4efc707b <unknown>\n#4 0x5a8f4f0069ad <unknown>\n#5 0x5a8f4f00618f <unknown>\n#6 0x5a8f4effd9a3 <unknown>\n#7 0x5a8f4efd246a <unknown>\n#8 0x5a8f4efd355e <unknown>\n#9 0x5a8f4f22ccae <unknown>\n#10 0x5a8f4f2308fe <unknown>\n#11 0x5a8f4f239f20 <unknown>\n#12 0x5a8f4f231923 <unknown>\n#13 0x5a8f4f204c0e <unknown>\n#14 0x5a8f4f254b08 <unknown>\n#15 0x5a8f4f254c97 <unknown>\n#16 0x5a8f4f265113 <unknown>\n#17 0x796c46040ac3 <unknown>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import requests\n",
        "from bs4 import BeautifulSoup\n",
        "\n",
        "# آدرس صفحه وب\n",
        "url = \"https://www.google.com\"\n",
        "\n",
        "# ارسال درخواست به وب‌سایت\n",
        "response = requests.get(url)\n",
        "\n",
        "# بررسی وضعیت پاسخ\n",
        "if response.status_code == 200:\n",
        "    # پردازش HTML با BeautifulSoup\n",
        "    soup = BeautifulSoup(response.text, 'html.parser')\n",
        "\n",
        "    # نمایش عنوان صفحه\n",
        "    print(soup.title.string)\n",
        "else:\n",
        "    print(\"خطا در دریافت صفحه.\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "324nUSx-iY05",
        "outputId": "d608a2d6-7d9d-4b50-c4a0-a01db37e83a3"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Google\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import requests\n",
        "from bs4 import BeautifulSoup\n",
        "\n",
        "# آدرس صفحه وب\n",
        "url = \"https://www.google.com\"\n",
        "\n",
        "# ارسال درخواست به وب‌سایت\n",
        "response = requests.get(url)\n",
        "\n",
        "# بررسی وضعیت پاسخ\n",
        "if response.status_code == 200:\n",
        "    # پردازش HTML با BeautifulSoup\n",
        "    soup = BeautifulSoup(response.text, 'html.parser')\n",
        "\n",
        "    # استخراج تمام لینک‌ها\n",
        "    links = soup.find_all('a')\n",
        "\n",
        "    # نمایش لینک‌ها\n",
        "    for link in links:\n",
        "        print(link.get('href'))\n",
        "else:\n",
        "    print(\"خطا در دریافت صفحه.\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "49rm8YO7igaD",
        "outputId": "82c9a394-e0e2-4c32-f18a-008fc0ff3323"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "https://www.google.com/imghp?hl=en&tab=wi\n",
            "https://maps.google.com/maps?hl=en&tab=wl\n",
            "https://play.google.com/?hl=en&tab=w8\n",
            "https://www.youtube.com/?tab=w1\n",
            "https://news.google.com/?tab=wn\n",
            "https://mail.google.com/mail/?tab=wm\n",
            "https://drive.google.com/?tab=wo\n",
            "https://www.google.com/intl/en/about/products?tab=wh\n",
            "http://www.google.com/history/optout?hl=en\n",
            "/preferences?hl=en\n",
            "https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ\n",
            "/advanced_search?hl=en&authuser=0\n",
            "/intl/en/ads/\n",
            "/services/\n",
            "/intl/en/about.html\n",
            "/intl/en/policies/privacy/\n",
            "/intl/en/policies/terms/\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install chatterbot\n",
        "!pip install chatterbot_corpus\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "KJiD10Q2jLN9",
        "outputId": "b478dfc2-0c5a-46d1-b357-96861d3ec5c0"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting chatterbot\n",
            "  Downloading chatterbot-1.2.3-py3-none-any.whl.metadata (8.5 kB)\n",
            "Collecting mathparse<0.2,>=0.1 (from chatterbot)\n",
            "  Downloading mathparse-0.1.2-py3-none-any.whl.metadata (776 bytes)\n",
            "Collecting python-dateutil<2.10,>=2.9 (from chatterbot)\n",
            "  Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)\n",
            "Requirement already satisfied: sqlalchemy<2.1,>=2.0 in /usr/local/lib/python3.11/dist-packages (from chatterbot) (2.0.38)\n",
            "Collecting spacy<3.9,>=3.8 (from chatterbot)\n",
            "  Downloading spacy-3.8.4-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (27 kB)\n",
            "Requirement already satisfied: tqdm in /usr/local/lib/python3.11/dist-packages (from chatterbot) (4.67.1)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.11/dist-packages (from python-dateutil<2.10,>=2.9->chatterbot) (1.17.0)\n",
            "Requirement already satisfied: spacy-legacy<3.1.0,>=3.0.11 in /usr/local/lib/python3.11/dist-packages (from spacy<3.9,>=3.8->chatterbot) (3.0.12)\n",
            "Requirement already satisfied: spacy-loggers<2.0.0,>=1.0.0 in /usr/local/lib/python3.11/dist-packages (from spacy<3.9,>=3.8->chatterbot) (1.0.5)\n",
            "Requirement already satisfied: murmurhash<1.1.0,>=0.28.0 in /usr/local/lib/python3.11/dist-packages (from spacy<3.9,>=3.8->chatterbot) (1.0.12)\n",
            "Requirement already satisfied: cymem<2.1.0,>=2.0.2 in /usr/local/lib/python3.11/dist-packages (from spacy<3.9,>=3.8->chatterbot) (2.0.11)\n",
            "Requirement already satisfied: preshed<3.1.0,>=3.0.2 in /usr/local/lib/python3.11/dist-packages (from spacy<3.9,>=3.8->chatterbot) (3.0.9)\n",
            "Collecting thinc<8.4.0,>=8.3.4 (from spacy<3.9,>=3.8->chatterbot)\n",
            "  Downloading thinc-8.3.4-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (15 kB)\n",
            "Requirement already satisfied: wasabi<1.2.0,>=0.9.1 in /usr/local/lib/python3.11/dist-packages (from spacy<3.9,>=3.8->chatterbot) (1.1.3)\n",
            "Requirement already satisfied: srsly<3.0.0,>=2.4.3 in /usr/local/lib/python3.11/dist-packages (from spacy<3.9,>=3.8->chatterbot) (2.5.1)\n",
            "Requirement already satisfied: catalogue<2.1.0,>=2.0.6 in /usr/local/lib/python3.11/dist-packages (from spacy<3.9,>=3.8->chatterbot) (2.0.10)\n",
            "Requirement already satisfied: weasel<0.5.0,>=0.1.0 in /usr/local/lib/python3.11/dist-packages (from spacy<3.9,>=3.8->chatterbot) (0.4.1)\n",
            "Requirement already satisfied: typer<1.0.0,>=0.3.0 in /usr/local/lib/python3.11/dist-packages (from spacy<3.9,>=3.8->chatterbot) (0.15.2)\n",
            "Requirement already satisfied: numpy>=1.19.0 in /usr/local/lib/python3.11/dist-packages (from spacy<3.9,>=3.8->chatterbot) (1.26.4)\n",
            "Requirement already satisfied: requests<3.0.0,>=2.13.0 in /usr/local/lib/python3.11/dist-packages (from spacy<3.9,>=3.8->chatterbot) (2.32.3)\n",
            "Requirement already satisfied: pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4 in /usr/local/lib/python3.11/dist-packages (from spacy<3.9,>=3.8->chatterbot) (2.10.6)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.11/dist-packages (from spacy<3.9,>=3.8->chatterbot) (3.1.6)\n",
            "Requirement already satisfied: setuptools in /usr/local/lib/python3.11/dist-packages (from spacy<3.9,>=3.8->chatterbot) (75.1.0)\n",
            "Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.11/dist-packages (from spacy<3.9,>=3.8->chatterbot) (24.2)\n",
            "Requirement already satisfied: langcodes<4.0.0,>=3.2.0 in /usr/local/lib/python3.11/dist-packages (from spacy<3.9,>=3.8->chatterbot) (3.5.0)\n",
            "Requirement already satisfied: greenlet!=0.4.17 in /usr/local/lib/python3.11/dist-packages (from sqlalchemy<2.1,>=2.0->chatterbot) (3.1.1)\n",
            "Requirement already satisfied: typing-extensions>=4.6.0 in /usr/local/lib/python3.11/dist-packages (from sqlalchemy<2.1,>=2.0->chatterbot) (4.12.2)\n",
            "Requirement already satisfied: language-data>=1.2 in /usr/local/lib/python3.11/dist-packages (from langcodes<4.0.0,>=3.2.0->spacy<3.9,>=3.8->chatterbot) (1.3.0)\n",
            "Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.11/dist-packages (from pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4->spacy<3.9,>=3.8->chatterbot) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.27.2 in /usr/local/lib/python3.11/dist-packages (from pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4->spacy<3.9,>=3.8->chatterbot) (2.27.2)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests<3.0.0,>=2.13.0->spacy<3.9,>=3.8->chatterbot) (3.4.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests<3.0.0,>=2.13.0->spacy<3.9,>=3.8->chatterbot) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests<3.0.0,>=2.13.0->spacy<3.9,>=3.8->chatterbot) (2.3.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests<3.0.0,>=2.13.0->spacy<3.9,>=3.8->chatterbot) (2025.1.31)\n",
            "Collecting blis<1.3.0,>=1.2.0 (from thinc<8.4.0,>=8.3.4->spacy<3.9,>=3.8->chatterbot)\n",
            "  Downloading blis-1.2.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (7.7 kB)\n",
            "Requirement already satisfied: confection<1.0.0,>=0.0.1 in /usr/local/lib/python3.11/dist-packages (from thinc<8.4.0,>=8.3.4->spacy<3.9,>=3.8->chatterbot) (0.1.5)\n",
            "Requirement already satisfied: click>=8.0.0 in /usr/local/lib/python3.11/dist-packages (from typer<1.0.0,>=0.3.0->spacy<3.9,>=3.8->chatterbot) (8.1.8)\n",
            "Requirement already satisfied: shellingham>=1.3.0 in /usr/local/lib/python3.11/dist-packages (from typer<1.0.0,>=0.3.0->spacy<3.9,>=3.8->chatterbot) (1.5.4)\n",
            "Requirement already satisfied: rich>=10.11.0 in /usr/local/lib/python3.11/dist-packages (from typer<1.0.0,>=0.3.0->spacy<3.9,>=3.8->chatterbot) (13.9.4)\n",
            "Requirement already satisfied: cloudpathlib<1.0.0,>=0.7.0 in /usr/local/lib/python3.11/dist-packages (from weasel<0.5.0,>=0.1.0->spacy<3.9,>=3.8->chatterbot) (0.21.0)\n",
            "Requirement already satisfied: smart-open<8.0.0,>=5.2.1 in /usr/local/lib/python3.11/dist-packages (from weasel<0.5.0,>=0.1.0->spacy<3.9,>=3.8->chatterbot) (7.1.0)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.11/dist-packages (from jinja2->spacy<3.9,>=3.8->chatterbot) (3.0.2)\n",
            "Requirement already satisfied: marisa-trie>=1.1.0 in /usr/local/lib/python3.11/dist-packages (from language-data>=1.2->langcodes<4.0.0,>=3.2.0->spacy<3.9,>=3.8->chatterbot) (1.2.1)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.11/dist-packages (from rich>=10.11.0->typer<1.0.0,>=0.3.0->spacy<3.9,>=3.8->chatterbot) (3.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.11/dist-packages (from rich>=10.11.0->typer<1.0.0,>=0.3.0->spacy<3.9,>=3.8->chatterbot) (2.18.0)\n",
            "Requirement already satisfied: wrapt in /usr/local/lib/python3.11/dist-packages (from smart-open<8.0.0,>=5.2.1->weasel<0.5.0,>=0.1.0->spacy<3.9,>=3.8->chatterbot) (1.17.2)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.11/dist-packages (from markdown-it-py>=2.2.0->rich>=10.11.0->typer<1.0.0,>=0.3.0->spacy<3.9,>=3.8->chatterbot) (0.1.2)\n",
            "Downloading chatterbot-1.2.3-py3-none-any.whl (72 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m72.8/72.8 kB\u001b[0m \u001b[31m3.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading mathparse-0.1.2-py3-none-any.whl (7.2 kB)\n",
            "Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m229.9/229.9 kB\u001b[0m \u001b[31m8.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading spacy-3.8.4-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (30.6 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m30.6/30.6 MB\u001b[0m \u001b[31m31.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading thinc-8.3.4-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.9 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m3.9/3.9 MB\u001b[0m \u001b[31m62.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading blis-1.2.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (11.7 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m11.7/11.7 MB\u001b[0m \u001b[31m44.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: mathparse, python-dateutil, blis, thinc, spacy, chatterbot\n",
            "  Attempting uninstall: python-dateutil\n",
            "    Found existing installation: python-dateutil 2.8.2\n",
            "    Uninstalling python-dateutil-2.8.2:\n",
            "      Successfully uninstalled python-dateutil-2.8.2\n",
            "  Attempting uninstall: blis\n",
            "    Found existing installation: blis 0.7.11\n",
            "    Uninstalling blis-0.7.11:\n",
            "      Successfully uninstalled blis-0.7.11\n",
            "  Attempting uninstall: thinc\n",
            "    Found existing installation: thinc 8.2.5\n",
            "    Uninstalling thinc-8.2.5:\n",
            "      Successfully uninstalled thinc-8.2.5\n",
            "  Attempting uninstall: spacy\n",
            "    Found existing installation: spacy 3.7.5\n",
            "    Uninstalling spacy-3.7.5:\n",
            "      Successfully uninstalled spacy-3.7.5\n",
            "\u001b[31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.\n",
            "en-core-web-sm 3.7.1 requires spacy<3.8.0,>=3.7.2, but you have spacy 3.8.4 which is incompatible.\u001b[0m\u001b[31m\n",
            "\u001b[0mSuccessfully installed blis-1.2.0 chatterbot-1.2.3 mathparse-0.1.2 python-dateutil-2.9.0.post0 spacy-3.8.4 thinc-8.3.4\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "application/vnd.colab-display-data+json": {
              "pip_warning": {
                "packages": [
                  "dateutil"
                ]
              },
              "id": "51853486d3fc4e0c94ae4521c61decd8"
            }
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting chatterbot_corpus\n",
            "  Downloading chatterbot_corpus-1.2.2-py2.py3-none-any.whl.metadata (1.1 kB)\n",
            "Downloading chatterbot_corpus-1.2.2-py2.py3-none-any.whl (240 kB)\n",
            "\u001b[?25l   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m0.0/240.5 kB\u001b[0m \u001b[31m?\u001b[0m eta \u001b[36m-:--:--\u001b[0m\r\u001b[2K   \u001b[91m━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[91m╸\u001b[0m\u001b[90m━━━━━━━━━━━━━━\u001b[0m \u001b[32m153.6/240.5 kB\u001b[0m \u001b[31m4.4 MB/s\u001b[0m eta \u001b[36m0:00:01\u001b[0m\r\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m240.5/240.5 kB\u001b[0m \u001b[31m4.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: chatterbot_corpus\n",
            "Successfully installed chatterbot_corpus-1.2.2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from chatterbot import ChatBot\n",
        "from chatterbot.trainers import ChatterBotCorpusTrainer\n",
        "\n",
        "# ایجاد ربات\n",
        "chatbot = ChatBot('SBCBot')\n",
        "\n",
        "# آموزش ربات با استفاده از داده‌های پیش‌فرض\n",
        "trainer = ChatterBotCorpusTrainer(chatbot)\n",
        "trainer.train('chatterbot.corpus.english')  # یا می‌تونی از زبان‌های دیگه استفاده کنی\n",
        "\n",
        "# آزمایش ربات\n",
        "response = chatbot.get_response(\"How do I solve SBC?\")\n",
        "print(response)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rwsBOI8bjSJo",
        "outputId": "371a54ad-b2b3-4bd3-e2ae-c0d1a7bad2ed"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.11/dist-packages/spacy/util.py:910: UserWarning: [W095] Model 'en_core_web_sm' (3.7.1) was trained with spaCy v3.7.2 and may not be 100% compatible with the current version (3.8.4). If you see errors or degraded performance, download a newer compatible model or retrain your custom model with the current spaCy version. For more details and available updates, run: python -m spacy validate\n",
            "  warnings.warn(warn_msg)\n",
            "ChatterBot Corpus Trainer: 19it [00:05,  3.57it/s]"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "happily you\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# مثال ساده از داده‌های بازیکنان و SBC‌ها\n",
        "players = {\n",
        "    \"player1\": {\"overall\": 85, \"position\": \"Forward\"},\n",
        "    \"player2\": {\"overall\": 88, \"position\": \"Midfielder\"},\n",
        "    # دیگر بازیکنان...\n",
        "}\n",
        "\n",
        "sbc_challenges = {\n",
        "    \"SBC1\": {\"required_overall\": 80, \"position_needed\": \"Forward\", \"tasks\": [\"Task1\", \"Task2\"]},\n",
        "    \"SBC2\": {\"required_overall\": 85, \"position_needed\": \"Midfielder\", \"tasks\": [\"Task1\", \"Task3\"]},\n",
        "    # دیگر SBC‌ها...\n",
        "}\n",
        "\n",
        "# تابعی برای پیشنهاد دادن SBC بر اساس بازیکنان\n",
        "def suggest_sbc(player):\n",
        "    for sbc, details in sbc_challenges.items():\n",
        "        if details[\"required_overall\"] <= player[\"overall\"] and details[\"position_needed\"] == player[\"position\"]:\n",
        "            return sbc, details[\"tasks\"]\n",
        "    return \"No suitable SBC found\", []\n",
        "\n",
        "# تست کردن با یکی از بازیکنان\n",
        "player_info = players[\"player1\"]\n",
        "sbc, tasks = suggest_sbc(player_info)\n",
        "\n",
        "print(f\"Suggested SBC: {sbc}\")\n",
        "print(f\"Tasks to complete: {tasks}\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Z1i3lDvmjawS",
        "outputId": "73dd0289-0be8-408b-dfa2-c47dfdb9051c"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Suggested SBC: SBC1\n",
            "Tasks to complete: ['Task1', 'Task2']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install streamlit\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nXTG997Ejc5e",
        "outputId": "0fffafd0-10fc-40e5-9a73-bd393a688e55"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting streamlit\n",
            "  Downloading streamlit-1.43.1-py2.py3-none-any.whl.metadata (8.9 kB)\n",
            "Requirement already satisfied: altair<6,>=4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.5.0)\n",
            "Requirement already satisfied: blinker<2,>=1.0.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (1.9.0)\n",
            "Requirement already satisfied: cachetools<6,>=4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.5.2)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (8.1.8)\n",
            "Requirement already satisfied: numpy<3,>=1.23 in /usr/local/lib/python3.11/dist-packages (from streamlit) (1.26.4)\n",
            "Requirement already satisfied: packaging<25,>=20 in /usr/local/lib/python3.11/dist-packages (from streamlit) (24.2)\n",
            "Requirement already satisfied: pandas<3,>=1.4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (2.2.2)\n",
            "Requirement already satisfied: pillow<12,>=7.1.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (11.1.0)\n",
            "Requirement already satisfied: protobuf<6,>=3.20 in /usr/local/lib/python3.11/dist-packages (from streamlit) (4.25.6)\n",
            "Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (18.1.0)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.11/dist-packages (from streamlit) (2.32.3)\n",
            "Requirement already satisfied: tenacity<10,>=8.1.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (9.0.0)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.11/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (4.12.2)\n",
            "Collecting watchdog<7,>=2.1.5 (from streamlit)\n",
            "  Downloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl.metadata (44 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m44.3/44.3 kB\u001b[0m \u001b[31m1.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.11/dist-packages (from streamlit) (3.1.44)\n",
            "Collecting pydeck<1,>=0.8.0b4 (from streamlit)\n",
            "  Downloading pydeck-0.9.1-py2.py3-none-any.whl.metadata (4.1 kB)\n",
            "Requirement already satisfied: tornado<7,>=6.0.3 in /usr/local/lib/python3.11/dist-packages (from streamlit) (6.4.2)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.11/dist-packages (from altair<6,>=4.0->streamlit) (3.1.6)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.11/dist-packages (from altair<6,>=4.0->streamlit) (4.23.0)\n",
            "Requirement already satisfied: narwhals>=1.14.2 in /usr/local/lib/python3.11/dist-packages (from altair<6,>=4.0->streamlit) (1.29.1)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.11/dist-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.11/dist-packages (from pandas<3,>=1.4.0->streamlit) (2.9.0.post0)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.11/dist-packages (from pandas<3,>=1.4.0->streamlit) (2025.1)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.11/dist-packages (from pandas<3,>=1.4.0->streamlit) (2025.1)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (3.4.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (2.3.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (2025.1.31)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.11/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.2)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.11/dist-packages (from jinja2->altair<6,>=4.0->streamlit) (3.0.2)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (25.1.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2024.10.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.36.2)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.23.1)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.11/dist-packages (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit) (1.17.0)\n",
            "Downloading streamlit-1.43.1-py2.py3-none-any.whl (9.7 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m9.7/9.7 MB\u001b[0m \u001b[31m52.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.9/6.9 MB\u001b[0m \u001b[31m69.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl (79 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m79.1/79.1 kB\u001b[0m \u001b[31m4.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: watchdog, pydeck, streamlit\n",
            "Successfully installed pydeck-0.9.1 streamlit-1.43.1 watchdog-6.0.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "\n",
        "# رابط کاربری برای ورودی بازیکن و پیشنهاد SBC\n",
        "st.title(\"EAFC25 SBC Solver\")\n",
        "\n",
        "# ورودی‌های بازیکن\n",
        "player_name = st.text_input(\"Enter your player name:\")\n",
        "player_overall = st.number_input(\"Enter player overall rating:\", min_value=60, max_value=99)\n",
        "player_position = st.selectbox(\"Select player position:\", [\"Forward\", \"Midfielder\", \"Defender\", \"Goalkeeper\"])\n",
        "\n",
        "# نمایش پیشنهادات\n",
        "if st.button(\"Suggest SBC\"):\n",
        "    player_info = {\"overall\": player_overall, \"position\": player_position}\n",
        "    sbc, tasks = suggest_sbc(player_info)\n",
        "\n",
        "    st.write(f\"Suggested SBC: {sbc}\")\n",
        "    st.write(f\"Tasks to complete: {tasks}\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2yPo9q6njfiJ",
        "outputId": "e0a2efa4-2cf9-4145-8d71-caecc8102900"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2025-03-11 14:13:48.122 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-11 14:13:48.300 \n",
            "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
            "  command:\n",
            "\n",
            "    streamlit run /usr/local/lib/python3.11/dist-packages/colab_kernel_launcher.py [ARGUMENTS]\n",
            "2025-03-11 14:13:48.303 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-11 14:13:48.305 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-11 14:13:48.306 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-11 14:13:48.307 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-11 14:13:48.307 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-11 14:13:48.308 Session state does not function when running a script without `streamlit run`\n",
            "2025-03-11 14:13:48.309 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-11 14:13:48.310 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-11 14:13:48.311 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-11 14:13:48.313 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-11 14:13:48.314 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-11 14:13:48.314 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-11 14:13:48.317 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-11 14:13:48.318 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-11 14:13:48.319 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-11 14:13:48.321 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-11 14:13:48.322 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-11 14:13:48.323 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-11 14:13:48.326 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-11 14:13:48.326 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-11 14:13:48.327 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-11 14:13:48.328 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-11 14:13:48.329 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-11 14:13:48.330 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-11 14:13:48.333 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ]
    }
  ]
}
