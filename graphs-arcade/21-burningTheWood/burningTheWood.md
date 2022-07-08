<p>You've been walking in the woods you got so attached to for the entire day. The weather was nice and warm, the smell of the nature was wonderful, and you got so carried away (both literally and virtually) that didn't even notice when it started to get cold. Your home is too far from your current location, and you're barely standing on your feet having walked for so long, so you have no other option but to make your bed right where you are.</p>
<p>Since it's really cold already, you'd like to start a campfire. Of course playing with fire is a bad idea, especially in dry woods, but you didn't sleep last night and need at least <code>k</code> hours of sleep to think straight the next day. You assume that if the fire starts in some meadow, each hour it'll spread to all the neighboring meadows, each of which will in turn set their neighboring meadows on fire in another hour.</p>
<p>There are <code>n</code> meadows in the forest, and you're going to start a campfire in your current meadow <code>start</code>. Knowing how the meadows are connected (this information is given as a matrix <code>wmap</code>), find out which meadows may be on fire when you wake up after <code>k</code> hours and return the list of these meadows sorted in ascending order (don't worry about yourself - woods around you are not dry, so the fire in your meadow won't hurt you).</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>n = 5</code>, <code>wmap = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]</code>,<br />
<code>start = 0</code>, and <code>k = 1</code>, the output should be<br />
<code>solution(n, wmap, start, k) = [0, 1, 4]</code>.</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/burningTheWood/img/example1.png?_tm=1624426142769" alt /></p>
</li>
<li>
<p>For <code>n = 7</code>,</p>
<pre><code>wmap = [[0, 1], [1, 2], [2, 3], [3, 4], 
         [4, 5], [5, 6], [6, 0], [4, 1]]
</code></pre>
<p><code>start = 0</code>, and <code>k = 2</code>, the output should be<br />
<code>solution(n, wmap, start, k) = [0, 1, 2, 4, 5, 6]</code>.</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/burningTheWood/img/example2.png?_tm=1624426143055" alt /></p>
<p>At the beginning of the first hour meadow <code>0</code> starts burning. At the second hour meadows <code>1</code> and <code>6</code> start burning as well. At the third hour neighbors of meadow <code>1</code> - meadows <code>2</code> and <code>4</code> - catch on fire, and so does the only neighbor of meadow <code>6</code> - meadow <code>5</code>. So, at the end of the third hour meadows <code>0</code>, <code>1</code>, <code>2</code>, <code>4</code>, <code>5</code> and <code>6</code> will be on fire.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer n</strong></p>
<p>The number of meadows in the forest.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ n ≤ 5 · 10<sup>4</sup></code>.</p>
</li>
<li>
<p><strong>[input] array.array.integer wmap</strong></p>
<p>The information about the connected meadows. <code>wmap[i]</code> for each valid <code>i</code> contains two elements and represents a road that connects <code>wmap[i][0]</code> and <code>wmap[i][1]</code>.<br />
It is guaranteed that between any two vertices there is no more than one edge.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ wmap.length ≤ 5 · 10<sup>4</sup></code>,<br />
<code>wmap[i].length = 2</code>,<br />
<code>0 ≤ wmap[i][j] &lt; n</code>.</p>
</li>
<li>
<p><strong>[input] integer start</strong></p>
<p>The meadow where you're going to start a campfire.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ start &lt; n</code>.</p>
</li>
<li>
<p><strong>[input] integer k</strong></p>
<p>The number of hours you're going to sleep.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ k ≤ 10<sup>3</sup></code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
<p>The list of meadows that may be on fire in <code>k</code> hours sorted in ascending order.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
