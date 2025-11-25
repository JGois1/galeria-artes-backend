import azure.functions as func
import logging
import os
import json
import psycopg2

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="obter_obras")
def obter_obras(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processando requisição para obter obras.')

    try:
        conn = psycopg2.connect(
            host=os.environ["DB_HOST"],
            database=os.environ["DB_NAME"],
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASS"],
            sslmode="require"
        )
        
        cur = conn.cursor()
        cur.execute("SELECT id, nome, artista, descricao, url_imagem FROM obras")
        rows = cur.fetchall()

        obras_lista = []
        for row in rows:
            obra = {
                "id": row[0],
                "nome": row[1],
                "artista": row[2],
                "descricao": row[3],
                "url_imagem": row[4]
            }
            obras_lista.append(obra)

        cur.close()
        conn.close()

        return func.HttpResponse(
            json.dumps(obras_lista),
            mimetype="application/json",
            status_code=200
        )

    except Exception as e:
        logging.error(f"Erro ao conectar no banco: {str(e)}")
        return func.HttpResponse(
            f"Erro interno: {str(e)}",
            status_code=500
        )