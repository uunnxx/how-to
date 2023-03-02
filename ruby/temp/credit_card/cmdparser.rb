require 'creditcard'
require 'cmdparse'

cmd = CmdParse::CommandParser.new(true, true)
cmd.program_name = "creditcard_check"
cmd.program_version = [0, 2, 0]
cmd.add_command(CmdParse::HelpCommand.new, true)
cmd.add_command(CmdParse::VersionCommand.new, true)

verify = CmdParse::Command.new('verify', false)
verify.short_desc = "Verifies a credit card"
verify.set_execution_block do |args|
  args.each do |arg|
    if arg.creditcard?
      puts "Valid"
    else
      puts "Invalid"
    end
  end
end

type = CmdParse::Command.new('type', false)
type.short_desc = "Returns the type of credit card"
type.set_execution_block do |args|
  args.each do |arg|
    if arg.creditcard?
      puts arg.creditcard_type
    else
      puts "Invalid"
    end

  end
end

cmd.add_command(verify, false)
cmd.add_command(type, false)
cmd.parse
