import optparse

parser=optparse.OptionParse()

parser.add_option ("-r","--result",help="you can get the result from this command" )


options = parser.parse_args()
