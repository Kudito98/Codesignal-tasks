<p>You've launched your brand new web application not long ago, and while in beta it got <code>beta</code> satisfied visitors. Encouraged by such success, you decided to go ahead and push the very first stable version live.</p>
<p>You know that each <code>beta</code> visitor spent at least <code>k</code> minutes on your app, so now you'd like to keep track of new <code>visitors</code> of your web application that spent at least <code>k</code> minutes on it. Given the amount of time the <code>visitors</code> used your application and the value of <code>k</code>, return the total number of users that used your app for at least <code>k</code> minutes including those from <code>beta</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>beta = 22</code>, <code>k = 5</code>, and <code>visitors = [4, 6, 6, 5, 2, 2, 5]</code>,<br />
the output should be<br />
<code>solution(beta, k, visitors) = 26</code>.</p>
<p><code>4</code> new visitors spent at least <code>5</code> minutes on your application, which summed up with <code>22</code> satisfied <code>beta</code> users gives <code>26</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer beta</strong></p>
<p>The number of satisfied users of the beta version.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ beta ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[input] integer k</strong></p>
<p>The minimum amount of time each satisfied beta visitor spent on your application.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ k ≤ 100</code>.</p>
</li>
<li>
<p><strong>[input] array.integer visitors</strong></p>
<p>An array of visitors, where <code>visitors[i]</code> is the number of minutes the <code>i<sup>th</sup></code> visitor spent on the app.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ visitors.length ≤ 100</code>,<br />
<code>1 ≤ visitors[i] ≤ 100</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The total number of visitors that spent at least <code>k</code> minutes on your app.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
