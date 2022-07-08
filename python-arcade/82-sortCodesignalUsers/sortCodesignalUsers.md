<p>At CodeSignal the users can get to the top of the leaderboard by earning XP (experience points) in different modes. The leaderboard is sorted by players XP in descending order, and in case of a tie - by their ids in ascending order.</p>
<p>Your task is to implement an algorithm that will return the state of the weekly leaderboard given a list of <code>users</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For</p>
<pre><code>users = [["warrior", "1", "1050"],
         ["Ninja!",  "21", "995"],
         ["recruit", "3", "995"]]
</code></pre>
<p>the output should be<br />
<code>solution(users) = ["warrior", "recruit", "Ninja!"]</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.array.string users</strong></p>
<p>A list of CodeSignal users, where each user is given in the format <code>[<em>username</em>, <em>id</em>, <em>xp</em>]</code>.<br />
It is guaranteed that all usernames and ids are unique.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ users.length ≤ 10<sup>4</sup></code>,<br />
<code>users[i].length = 3</code>,<br />
<code>1 ≤ users[i][0].length ≤ 20</code>,<br />
<code>1 ≤ int(users[i][1]), int(users[i][2]) ≤ 10<sup>4</sup></code>.</p>
</li>
<li>
<p><strong>[output] array.string</strong></p>
<p>A list of CodeSignal users sorted as described above.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
