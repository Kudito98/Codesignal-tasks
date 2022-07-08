<p>You've just started to study impartial games, and came across an interesting theory. The theory is quite complicated, but it can be narrowed down to the following statements: solutions to all such games can be found with the <em>mex</em> function. <em>Mex</em> is an abbreviation of <em>minimum excludant</em>: for the given set <code>s</code> it finds the minimum non-negative integer that is not present in <code>s</code>.</p>
<p>You don't yet know how to implement such a function efficiently, so would like to create a simplified version. For the given set <code>s</code> and given an <code>upperBound</code>, implement a function that will find its <em>mex</em> if it's smaller than <code>upperBound</code> or return <code>upperBound</code> instead.</p>
<p><em>Hint: <code>for</code> loops also have an <code>else</code> clause which executes when the loop completes normally, i.e. without encountering any <code>break</code>s</em></p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>s = [0, 4, 2, 3, 1, 7]</code> and <code>upperBound = 10</code>,<br />
the output should be<br />
<code>solution(s, upperBound) = 5</code>.</p>
<p><code>5</code> is the smallest non-negative integer that is not present in <code>s</code>, and it is smaller than <code>upperBound</code>.</p>
</li>
<li>
<p>For <code>s = [0, 4, 2, 3, 1, 7]</code> and <code>upperBound = 3</code>,<br />
the output should be<br />
<code>solution(s, upperBound) = 3</code>.</p>
<p>The minimum excludant for the given set is <code>5</code>, but it's greater than <code>upperBound</code>, so the output should be <code>3</code>.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.integer s</strong></p>
<p>Array of distinct non-negative integers.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ s.length ≤ 100</code>,<br />
<code>0 ≤ s[i] ≤ 100</code>.</p>
</li>
<li>
<p><strong>[input] integer upperBound</strong></p>
<p>A positive integer.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ upperBound ≤ 100</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p><em>Mex</em> of <code>s</code> if it's smaller than <code>upperBound</code>, or <code>upperBound</code> instead.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
