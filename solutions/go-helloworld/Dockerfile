FROM golang:alpine

WORKDIR /go/src/app

ADD . .

Run go mod init 

RUN go build  -o helloworld

EXPOSE 6111

CMD ["./helloworld"]

