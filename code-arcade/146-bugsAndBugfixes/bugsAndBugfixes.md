<p>In most role-playing games, die rolls required by the system are given in the form <code>AdX</code>. <code>A</code> and <code>X</code> are positive integers, separated by the letter <code>'d'</code>, which stands for <em>die</em> or <em>dice</em>.</p>
<ul>
<li><code>A</code> is the number of times the die should be rolled (usually omitted if <code>1</code>).</li>
<li><code>X</code> is the number of faces on the die.</li>
</ul>
<p>To this basic notation, an additive modifier can be appended that yields expressions in the form <code>AdX+B</code> or <code>AdX-B</code>. <code>B</code> is a number added to the sum of the rolls (or subtracted from it). So, <code>1d20-10</code> would indicate a single roll of a 20-sided die with 10 being subtracted from the result.</p>
<p>You're reading the <code>rules</code> of a famous <em>Bugs and Bugfixes</em> role-playing game involving dice. What is the maximum number of points you can get, assuming that you roll the dice according to each formula present within <code>rules</code>?</p>
<p>It is guaranteed that all the formulas that appear in <code>rules</code> are correct (i.e. <code>A</code> and <code>X</code> are always positive in a formula-like substring), and any two substrings that may be formulas do not overlap.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>rules = "Roll d6-3 and 4d4+3 to pick a weapon, and finish the boss with 3d7!"</code>,<br />
the output should be<br />
<code>solution(rules) = 43</code>.</p>
<p>There are three formulas in the <code>rules</code>.</p>
<ul>
<li><code>d6-3</code> indicates a single roll of a 6-sided die, with <code>3</code> subtracted from the result. The maximum number that is possible to get is thus <code>6 - 3 = 3</code>.</li>
<li><code>4d4+3</code> stands for <code>4</code> rolls of a 4-sided die, with <code>3</code> added to the result. It is possible to get <code>4 * 4 + 3 = 19</code> points.</li>
<li><code>3d7</code> means <code>3</code> rolls of a 7-sided die. The maximum number to obtain with it is <code>3 * 7 = 21</code>.</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string rules</strong></p>
<p>Rules given as a string.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ rules.length ≤ 100</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The maximum possible number of points. If there are no formulas in <code>rules</code>, the output should be <code>0</code>.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
