require 'katakata_irb' rescue nil

# https://github.com/ruby/reline/blob/master/doc/reline/face.md
Reline::Face.force_truecolor
Reline::Face.config(:completion_dialog) do |conf|
  conf.define :default, foreground: :yellow, background: :black
  conf.define :enhanced, foreground: :black, background: :yellow
  conf.define :scrollbar, foreground: :yellow, background: :black
end
