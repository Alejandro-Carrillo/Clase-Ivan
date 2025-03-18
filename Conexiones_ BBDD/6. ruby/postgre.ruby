require 'pg'

begin
    conn = PG.connect(host: 'localhost', user: 'postgres', password: '1234')
    puts "Conexión exitosa"
rescue PG::Error => e
    puts e.message
ensure
    conn.close if conn
end