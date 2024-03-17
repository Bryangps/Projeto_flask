from comunidadeimpressionadora import app, database
from comunidadeimpressionadora.models import Usuario
# #
# # with app.app_context():
# #     database.create_all()
#
# with app.app_context():
#     usuario = Usuario.query.filter_by(username='Novo bryan').first()
#     print(usuario.username)
#     print(usuario.email)
#     print(usuario.senha)




# with app.app_context():
#     usuario = Usuario(username='Bryan', email='bryan.gps@gmail.com', senha='12254444')
#     usuario2 = Usuario(username='Silva', email='bryan@gmail.com', senha='12244')
#     database.session.add(usuario)
#     database.session.add(usuario2)
#     database.session.commit()

# with app.app_context():
#     meus_usuarios = Usuario.query.first()
#     print(meus_usuarios.email)
#     print(meus_usuarios.posts)


# with app.app_context():
#     meu_psot = Post(id_usuario=1, titulo='Primeiro Post do Bryan', corpo='Bryan, wello word')
#     database.session.add(meu_psot)
#     database.session.commit()

# with app.app_context():
#     post = Post.query.first()
#     print(post.titulo)
#     print(post.autor.username)

with app.app_context():
    database.drop_all()
    database.create_all()

