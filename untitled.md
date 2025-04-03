<!DOCTYPE html>
<html>
<head>
    <title>Vestaboard</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <div class="board">
        {% for row in board %}
        <div class="row">
            {% for tile in row %}
            <div class="tile {{ tile.color }}">{{ tile.char }}</div>
            {% endfor %}
        </div>
        {% endfor %}
    </div>
</body>
</html>