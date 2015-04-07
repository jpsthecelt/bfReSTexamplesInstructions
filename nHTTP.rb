require 'net/http'

uri = URI('https://localhost:52311/api/login')
#uri2 = URI('https://localhost:52311/api/fixlets/master')
uri2 = URI('http://localhost:52311/api/fixlets/external/BES%20Support')

Net::HTTP.start(uri.host, uri.port,
  :use_ssl => uri.scheme == 'https', :verify_mode => OpenSSL::SSL::VERIFY_NONE) do |http|

  request = Net::HTTP::Get.new uri.request_uri
  request.basic_auth 'adminMO', 'adminmo'

  response = http.request request # Net::HTTPResponse object

  puts response
  puts response.body
end

  Net::HTTP.start(uri2.host, uri2.port,
  :use_ssl => uri.scheme == 'https', :verify_mode => OpenSSL::SSL::VERIFY_NONE) do |http|

  request = Net::HTTP::Get.new uri2.request_uri
  request.basic_auth 'adminMO', 'adminmo'

  response = {}
  response = http.request request # Net::HTTPResponse object

  puts response
  puts response.body
end
