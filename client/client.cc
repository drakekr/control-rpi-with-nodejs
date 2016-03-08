/*
Date : 8. Mar. 2016
Author : Drake, Song
License : MIT
*/

#include <iostream>
#include <string>

extern "C" {
	#include "pifacedigital.h"
	#include <curl/curl.h>
	#include <unistd.h>
}

// - - - - - - - - - - - - - - - - - - - -

enum {
	ERROR_ARGS = 1 ,
	ERROR_CURL_INIT = 2
} ;

enum {
	OPTION_FALSE = 0 ,
	OPTION_TRUE = 1
} ;

enum {
	FLAG_DEFAULT = 0 
} ;

// - - - - - - - - - - - - - - - - - - - -

static size_t write_html(void *ptr, size_t size, size_t count, void *stream){ // 데이터 쓰기 함수
  ((std::string*)stream)->append((char*)ptr, 0, size*count); // stream에 문자열을 추가한다.
  return size*count;
}

bool http_get(const char *url, std::string &html)
{
  CURL *curl;
  CURLcode res;
  curl = curl_easy_init();
  if(curl) {
    curl_easy_setopt(curl, CURLOPT_URL, url); // url 변수를 GET 요청 주소로 사용
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_html); // 쓰기 함수에 write_html() 사용
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, &html); // 쓰기 데이터에 html을 사용 (stream)
    res = curl_easy_perform(curl);
    curl_easy_cleanup(curl);
    return true; // 성공하면 true 리턴
  } else {
    return false; // 실패하면 false 리턴
  }
}

int main(const int argc , const char** argv)
{
  const char* geturl = "https://data.drake.kr/piweb/status.dat";
  std::string status;

  int i = 0;
  uint8_t inputs;
  int hw_addr = 0;
  int interrupts_enabled;

  pifacedigital_open(hw_addr);

  //pifacedigital_write_reg(0x00, OUTPUT, hw_addr);

  while(1)
  {
    if(http_get(geturl, status)) 
    {
      for(i = 0; i < 8; i++)
      {
        if(status[i] == '1')
          pifacedigital_digital_write(i, 1);
        else
          pifacedigital_digital_write(i, 0);
      }
      sleep(1);
    }
    status = "";
  }
  return 0;
} // main()
