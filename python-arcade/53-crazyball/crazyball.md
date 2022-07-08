<p>You've been training your whole life, and now your dreams finally came true: you are a member of the best Crazyball team in the world! Unfortunately since your team is one of only two teams that play Crazyball, there are already many <code>players</code> in it, including yourself. For the starting lineup on the upcoming game the coach will pick <code>k</code> players, and you're curious if it's possible for you to make it there.</p>
<p>To calculate the odds of being a starter, you'd like to come up with a list of all possible lineups. Given the list of the <code>players</code> and the number of players <code>k</code> the coach has to pick, return all possible lineups sorted <a href="keyword://lexicographical-order-for-arrays" target="_blank">lexicographically</a>. Players in each lineup should also be sorted <a href="keyword://lexicographical-order-for-strings" target="_blank">lexicographically</a>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>players = ["Ninja", "Warrior", "Trainee", "Newbie"]</code> and <code>k = 3</code>,<br />
the output should be</p>
<pre><code>solution(players, k) = [["Newbie", "Ninja", "Trainee"], 
                         ["Newbie", "Ninja", "Warrior"], 
                         ["Newbie", "Trainee", "Warrior"], 
                         ["Ninja", "Trainee", "Warrior"]]
</code></pre>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.string players</strong></p>
<p>Array of distinct strings, where each string is player name. Each name may consist of English letters and whitespace characters.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ players.length ≤ 10</code>,<br />
<code>2 ≤ players[i].length ≤ 15</code>.</p>
</li>
<li>
<p><strong>[input] integer k</strong></p>
<p>The number of players the coach should pick for the lineup.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ k ≤ players.length</code>.</p>
</li>
<li>
<p><strong>[output] array.array.string</strong></p>
<p>Array of all possible lineups sorted as described above.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
