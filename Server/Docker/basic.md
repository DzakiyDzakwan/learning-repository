# DOCKER

Untuk melihat versi docker yang aktif dapat menggunakan perintah
`docker version`

## Docker Registry

- **Docker Registry** adalah tempat untuk menyimpan docker image
- Salah satu contoh dari salah satu docker registry adalah [https://hub.docker.com](https://hub.docker.com)

## Docker Image

- **Docker Image** mirip seperti installer aplikasi, dimana di dalam Docker Image terdapat aplikasi dan dependency, Docker image berguna dalam melakukan instalasi Docker Container
- Untuk melihat list image dapat menggunakan perintah
  `docker image ls`
- Untuk mendownload docker image dari docker registry dapat menggunakan perintah :  
  `docker image pull <nama_image>:<tag>`
- Untuk menghapus docker image dapat menggunakan perintah :
  `docker image rm <nama_image>:<image_tag>`

## Docker Container

- **Docker Container** mirip seperti aplikasi, yang mana harus dijalankan untuk digunakan.
- Docker Image yang digunakan pada instalasi Docker Container tidak dapat dihapus dikarenakan container tidak mengcopy isi yang ada didalam docker image, melainkan container hanya meminjam data yang diperlukan

- Untuk melihat container yang berjalan dapat menggunakan perintah
  `docker container ls`

- Untuk melihat container yang berjalan maupun tidak berjalan dapat menggunakan perintah
  `docker container ls -a`

- Untuk membuat container, kita bisa gunakan perintah:
  `docker container create --name <container_name> <image_name>:<image_tag>`
- Jika menggunakan image yang belum di download, maka docker akan secara otomatis mendowload image nya.

- Untuk menjalankan container dapat menggunakan perintah
  `docker container start <container_id/container_name>`

- Untuk menghentikan container dapat menggunakan perintah
  `docker container stop <container_id/container_name>`

- Untuk menghapus container dapat menggunakan perintah
  `docker container rm <container_id/container_name>`

- Untuk melihat logs container dapat menggunakan perintah
  `docker container logs <container_id/container_name>`
  dan untuk melihat log secara realtime dapat menggunakan
  `docker container logs -f <container_id/container_name>`

  ### Container Exec

- Saat menjalankan container, container terisolasi dalam docker sehingga host tidak dapat mengakses aplikasi yang ada di dalam container secara langsung. Untuk masuk kedalam container dan mengeksekusi perintah didalam container dapat menggunakan perintah
  `docker container exec -i -t <container_id/container_name> <command>`

### Container Port Fowarding

- Kita dapat melakukan port fowarding dari host ke docker container ketika membuat container dengan menggunakan perintah
  `docker container create --name <container_name> --publish <port_host>:<port_container> <image_name>:<image_tag>`

  - Port fowarding dapat dilakukan lebih dari satu dengan menambahkan dua kali parameter `--publish` dan parameter tersebut dapat disingkat menggukana `-p`

### Container Environment

-Docker container memiliki parameter yang bisa kita gunakan untuk mengirim environment variable ke aplikasi yang terdapat di dalam container, untuk mengirim environment variable tersebut dapat menggunakan perintah
`docker container create --bane <container_name> --env <key>=<value> <image_name>:<image_tag>`

- Sama seperti port fowarding, environment variable dapat ditambahkan lebih dari satu

### Container Stats

- Docker memiki kemampuan untuk melihat penggunaan resource dar tiap container yang sedang berjalan denga menggunakan perintah
  `docker container stats`

### Container Resource Limit

- Saat membuat container, secara default docker akan menggunakan CPU dan Memory yang diberikan ke Docker dan ankan menggunakan semua CPU dan Memory yang tersedia di sistem Host(Linux)
- Docker dapat memnetukan jumlah memory, cpu yang bisa digunakan oleh container dengan menggukan perintah
  `docker container create --bane <container_name> --memory <memory_number> --cpus <cpu_number> <image_name>:<image_tag>`

## Docker Bind Mount and Volume

- Docker bind mount merupakan fitur yang dapat dilakukan oleh docker untuk menyimpan data container didalam sistem host, fitur bind mount dapat dilakukan denga menggunakan command
  `docker container create --bane <container_name> --mount"type=bind,source=folder,destination=folder,readonly" <image_name>:<image_tag>`

- Docker Volume dapat dikatakan versi terbaru dari Bind Mount, bedanya pada Bind Mount data disimpan pada sistem host, sementara pada Volume data di atur oleh Docker sendiri.
- Saat membuat container secara default data disimpan didalam volume, untuk melihat daftar volume dapat menggunakan command
  `docker volume ls`

- Untuk membuat volume secara manual dapat menggunakan command
  `docker volume create <volume_name>`

- Untuk menghapus volume dapat dihapus dengan menggunakan command
  `docker volume rm <volume_name>`

- Keunutungan menggunakan volume adalah, jika container dihapus maka data akan tetap aman di volume
- Cara menghubungkan volume dengan container sama dengan bind mount hanya saja berbeda di type yang menggunakan tipe volume dan source dengan nama volume
  `docker container create --bane <container_name> --mount"type=volume,source=<volume_name>,destination=<container_source>,readonly" <image_name>:<image_tag>`

- Sampai saat ini belum ada cara otomatis untuk melakukan backup volume yang sudah dibuat, berbeda dengan bind mount yang data disimpan didalam sistem host. Namun kita dapat memanfaatkan backup menggunakan container
