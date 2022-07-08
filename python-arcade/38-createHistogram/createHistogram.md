<p>You noticed that one of your employees has a weird performance rate: although his performance is usually good and stable, from time to time it drops drastically. You suspect it has something to do with the famous Code of Clones series: new episodes started to come out recently, and everyone watches and rewatches them every so often.</p>
<p>To confirm your theory, you'd like to create a histogram showing the number of assignments he completed each day in the given period. Given this <code>assignments</code>, return a list representing a horizontal histogram, where each bar is formed by the given character <code>ch</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>ch = '*'</code> and <code>assignments = [12, 12, 14, 3, 12, 15, 14]</code>,<br />
the output should be</p>
<pre><code>solution(ch, assignments) = ["************",
                                    "************",
                                    "**************",
                                    "***",
                                    "************",
                                    "***************",
                                    "**************"]
</code></pre>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] char ch</strong></p>
<p>A character that should compose the histogram.</p>
</li>
<li>
<p><strong>[input] array.integer assignments</strong></p>
<p>A list of assignments your employee completed each day during some period.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ assignments.length ≤ 20</code>,<br />
<code>0 ≤ assignments[i] ≤ 50</code>.</p>
</li>
<li>
<p><strong>[output] array.string</strong></p>
<p>A histogram built as described above.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
