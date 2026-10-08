---
layout: default
title: Projects
permalink: /projects/
section: /research/
description: "Representative research projects of Ioannis Mitliagkas's group, grouped by area."
---
<div class="prose">
  <h1>Projects</h1>
  <p>Representative projects grouped by area. This archive was last curated in early 2022; see the <a href="{{ '/research/' | relative_url }}">research page</a> for current themes.</p>
</div>
{% for area in site.data.projects %}
<h2>{{ area.area }}</h2>
<ul class="projects">
  {% for it in area.items %}
  <li class="project">
    <a href="{{ it.url }}">{% if it.image %}<img src="{{ '/images/' | append: it.image | relative_url }}" alt="" loading="lazy">{% endif %}</a>
    <h3><a href="{{ it.url }}">{{ it.title }}</a></h3>
    <p>{{ it.summary }}</p>
    {% if it.lead %}<p>Lead: {{ it.lead }}</p>{% endif %}
  </li>
  {% endfor %}
</ul>
{% endfor %}
