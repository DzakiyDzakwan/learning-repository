# DOCKERFILE

-**Dockerfile** adalah rangkaian instruksi yang kita simpan untuk membuat Docker Image
- Untuk membuat Docker Image dari Dockerfile kita dapat menggunakan perintah 
`docker build -t <image_name>/<image_tag> <dockerfile_folder>`
- Untuk penamaan Dockerfile dibuat dengan nama `Dockerfile` saja tanpa menggunakan extension

## Instruction

- `#` digunakan untuk membuat komentar
- `INSTRUCTION` merupakan perintah yang digunakan di Dockerfile, untuk penulisan case insesitive namun direkomendasikan menggunakan Upper Case
- Arguments merupakan data argument untuk INSTRUCTION
- `FROM` digunakan untuk membuat build stage dari image yang kita tentukan. Kita akan jarang membuat Docker Image dari scratch melainkan kita akan membuat Docker Image dari Image yang sudah ada, berikut perintah menggunakan `FROM` :
`FROM <image>:<tag>`
- `RUN` sebuah instruksi untuk mengeksekusi perintah didalam image pada saat build stage, berikut perintah menggunkana `RUN` :
`RUN mkdir helloDirectories`
- Jika ingin melihat detail dapat menambahkan perintah `--progress=plain`
- Jikan ingin melakukan buil tanpa cahce dapat menambahkan perintah `--no-cache`
- `CMD` merupakan instruksi yang dijalankan ketika Docker Container berjalan
- Jika terdapat lebih dari satu instruksi `CMD`, maka container hanya akan menjalan instruksi `CMD` terakhir