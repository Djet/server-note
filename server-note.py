from bottle import route, run, request,post
import base64, os, git

dir_for_save = "/tmp/note-git/"
repo_dir = os.path.join(dir_for_save)
git_repo = git.Repo.init(dir_for_save)

@post('/<note_base64:path>')
def note(note_base64):
    note_path = note_base64.rstrip('/')
    base64_message = request.forms.get('base64').encode('ascii')
    message = base64.b64decode(base64_message).decode('ascii')
    filename = dir_for_save + note_path
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
    with open(filename, "w") as f:
       f.write(message)
    git_repo.index.add([filename])
    git_repo.index.commit("add new file")
    return "note created"

run(host='localhost', port=8010)