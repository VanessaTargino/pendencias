from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from pendencias.schemas import Message, UserSchema, UserPublic, UserDB, PendenciaCreate, Pendencia

app = FastAPI()

#banco em memória
user_db = []
pendencias_db = []

@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': ' API Pendências Funcionando'}

#cria usuário com id
@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):

    user_with_id = UserDB(
        id=len (user_db) +1,
        **user.model_dump()
    )

    user_db.append(user_with_id)

    return user_with_id


@app.get('/users/', response_model=list[UserPublic])
def list_users():
    return user_db

#cria pendencias de acordo com o usuário
@app.post('/pendencias/', status_code=HTTPStatus.CREATED)
def create_pendencia(pendencia: PendenciaCreate):

    usuario_existe = any(user.id == pendencia.usuario_id for user in user_db)

    if not usuario_existe:
        raise HTTPException(
            status_code=404,
            detail='Usuário não encontrado'
        )

    pendencia_with_id = {
        'id': len(pendencias_db) + 1,
        'concluida': False,
        **pendencia.model_dump()
    }

    pendencias_db.append(pendencia_with_id)

    return pendencia_with_id

#retorna todas as pendencias
@app.get('/pendencias/', response_model=list[Pendencia])
def list_pendencias():
    return pendencias_db

#retorna pendencia pelo id
@app.get('/pendencias/{pendencia_id}')
def get_pendencia(pendencia_id: int):

    for p in pendencias_db:
        if p['id'] == pendencia_id:
            return p

    raise HTTPException(
        status_code=404,
        detail='Pendência não encontrada'
    )

@app.get('/pendencias/{pendencia_id}', response_model=Pendencia)
def get_pendencia(pendencia_id: int):


    for p in pendencias_db:

        if p['id'] == pendencia_id:
            return p  

    raise HTTPException(
        status_code=404,
        detail='Pendência não encontrada'
    )
    
@app.put('/pendencias/{pendencia_id}', response_model=Pendencia)
def update_pendencia(pendencia_id: int, data: PendenciaCreate):

    for p in pendencias_db:
        if p['id'] == pendencia_id:
            p['titulo'] = data.titulo
            p['descricao'] = data.descricao
            p['usuario_id'] = data.usuario_id
            return p

    raise HTTPException(
        status_code=404,
        detail='Pendência não encontrada'
    )

@app.delete('/pendencias/{pendencia_id}')
def delete_pendencia(pendencia_id: int):

    for p in pendencias_db:
        if p['id'] == pendencia_id:
            pendencias_db.remove(p)
            return {'message': 'Pendência removida'}

    raise HTTPException(
        status_code=404,
        detail='Pendência não encontrada'
    )
