<p>To prepare his students for an upcoming game, the sports coach decides to try some new training drills. To begin with, he lines them up and starts with the following warm-up exercise: when the coach says <code>'L'</code>, he instructs the students to turn to the left. Alternatively, when he says <code>'R'</code>, they should turn to the right. Finally, when the coach says <code>'A'</code>, the students should turn around.</p>
<p>Unfortunately some students (not all of them, but at least one) can't tell left from right, meaning they always turn right when they hear <code>'L'</code> and left when they hear <code>'R'</code>. The coach wants to know how many times the students end up facing the same direction.</p>
<p>Given the list of commands the coach has given, count the number of such commands after which the students will be facing the same direction.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>commands = "LLARL"</code>, the output should be<br />
<code>solution(commands) = 3</code>.</p>
<p>Let's say that there are <code>4</code> students, and the second one can't tell left from right. In this case, only after the second, third and fifth commands will the students face the same direction.</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/lineUp/img/example.png?_tm=1582036863271" alt /></p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string commands</strong></p>
<p>String consisting of characters <code>'L'</code>, <code>'R'</code> and <code>'A'</code> only.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ commands.length ≤ 35</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The number of commands after which students face the same direction.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
