require "./nanospec.rb"


describe 'foo' do
  it 'speaks' do
    puts 'hi'
  end
end

describe 'bar' do
  it 'speaks' do
    puts 'hello'
  end

  it 'sleeps' do
    puts 'zzz'
  end
end
