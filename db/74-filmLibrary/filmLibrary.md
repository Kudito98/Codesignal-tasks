<p>You have a very big personal library of movies. You also have information about these movies stored in three tables - <code>movies</code>, <code>starring_actors</code>, and <code>actor_ages</code>. These tables have the following structures:</p>
<ul>
<li><strong>movies</strong>:
<ul>
<li><code>movie</code>: the unique name of the movie;</li>
<li><code>genre</code>: the genre of the movie.</li>
</ul>
</li>
<li><strong>starring_actors</strong>:
<ul>
<li><code>id</code>: the unique ID of the record;</li>
<li><code>movie_name</code>: the name of the movie;</li>
<li><code>actor</code>: the unique actor who stars in the movie. (You've made the decision to only add only one movie for each actor, the one in which they had the best role.)</li>
</ul>
</li>
<li><strong>actor_ages</strong>:
<ul>
<li><code>actor</code>: the unique name of the actor;</li>
<li><code>age</code>: the actor's age.</li>
</ul>
</li>
</ul>
<p>You've noticed that an actor usually only acts in the movies from one genre. And you believe that the older an actor is, the better they perform.</p>
<p>Now you don't know what to watch! So you decided to write a select statement that returns a list of actors, from oldest to youngest (if actors are the same age, sort them by name), who star in the movies in your favorite genre. (Your favorite genre is the most common one in your list of the movies, and it's guaranteed that only one such genre exists.) So now you can find the movies these actors star in, and there is a strong chance that these movies will be in your favorite genre.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For the following tables <strong>movies</strong></p>
<table>
<tr>
<th>movie</th>
<th>genre</th>
</tr>
<tr>
<td>Don't Breathe</td>
<td>crime movie</td>
</tr>
<tr>
<td>Drive</td>
<td>crime movie</td>
</tr>
<tr>
<td>Enemy</td>
<td>thriller</td>
</tr>
<tr>
<td>Mulholland Drive</td>
<td>mystery</td>
</tr>
<tr>
<td>Nocturnal Animals</td>
<td>thriller</td>
</tr>
<tr>
<td>The Neon Demon</td>
<td>thriller</td>
</tr>
</table>
<p><strong>starring_actors</strong>:</p>
<table>
<tr>
<th>id</th>
<th>movie_name</th>
<th>actor</th>
</tr>
<tr>
<td>1</td>
<td>Drive</td>
<td>Ryan Gosling</td>
</tr>
<tr>
<td>2</td>
<td>Drive</td>
<td>Carey Mulligan</td>
</tr>
<tr>
<td>3</td>
<td>Don't Breathe</td>
<td>Dylan Minnette</td>
</tr>
<tr>
<td>4</td>
<td>Enemy</td>
<td>Jake Gyllenhaal</td>
</tr>
<tr>
<td>5</td>
<td>Enemy</td>
<td>Sarah Gadon</td>
</tr>
<tr>
<td>6</td>
<td>Mulholland Drive</td>
<td>Naomi Watts</td>
</tr>
<tr>
<td>7</td>
<td>Mulholland Drive</td>
<td>Laura Harring</td>
</tr>
<tr>
<td>8</td>
<td>Nocturnal Animals</td>
<td>Amy Adams</td>
</tr>
<tr>
<td>9</td>
<td>Nocturnal Animals</td>
<td>Aaron Taylor-Johnson</td>
</tr>
<tr>
<td>10</td>
<td>Nocturnal Animals</td>
<td>Michael Shannon</td>
</tr>
<tr>
<td>11</td>
<td>The Neon Demon</td>
<td>Elle Fanning</td>
</tr>
<tr>
<td>12</td>
<td>The Neon Demon</td>
<td>Keanu Reeves</td>
</tr>
</table>
<p>and <strong>actor_ages</strong>:</p>
<table>
<tr>
<th>actor</th>
<th>age</th>
</tr>
<tr>
<td>Aaron Taylor-Johnson</td>
<td>26</td>
</tr>
<tr>
<td>Amy Adams</td>
<td>42</td>
</tr>
<tr>
<td>Carey Mulligan</td>
<td>31</td>
</tr>
<tr>
<td>Dylan Minnette</td>
<td>19</td>
</tr>
<tr>
<td>Elle Fanning</td>
<td>18</td>
</tr>
<tr>
<td>Jake Gyllenhaal</td>
<td>36</td>
</tr>
<tr>
<td>Keanu Reeves</td>
<td>52</td>
</tr>
<tr>
<td>Laura Harring</td>
<td>52</td>
</tr>
<tr>
<td>Michael Shannon</td>
<td>42</td>
</tr>
<tr>
<td>Naomi Watts</td>
<td>48</td>
</tr>
<tr>
<td>Ryan Gosling</td>
<td>36</td>
</tr>
<tr>
<td>Sarah Gadon</td>
<td>29</td>
</tr>
</table>
the output should be
<table>
<tr>
<th>actor</th>
<th>age</th>
</tr>
<tr>
<td>Keanu Reeves</td>
<td>52</td>
</tr>
<tr>
<td>Amy Adams</td>
<td>42</td>
</tr>
<tr>
<td>Michael Shannon</td>
<td>42</td>
</tr>
<tr>
<td>Jake Gyllenhaal</td>
<td>36</td>
</tr>
<tr>
<td>Sarah Gadon</td>
<td>29</td>
</tr>
<tr>
<td>Aaron Taylor-Johnson</td>
<td>26</td>
</tr>
<tr>
<td>Elle Fanning</td>
<td>18</td>
</tr>
</table>
<p>As you can see in the first table, the most common genre is "thriller" - it appears <code>3</code> times out of <code>6</code>. These <code>3</code> movies are "Enemy", "Nocturnal Animals", and "The Neon Demon". The actors starring in these movies are presented in the resulting table, sorted by ages.</p>
<ul>
<li><strong>[execution time limit] 10 seconds (mysql)</strong></li>
</ul>
