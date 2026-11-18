/* Local-only presentation helper. Load after markup; no network requests. */
(() => {
  const page = document.querySelector('[data-sketch]');
  if (!page) return;
  // A page can set html[data-theme] and may change it at any time; the CSS reads it.
  // Until the page sets it, follow the system theme. Never overwrite a value the page set.
  const root = document.documentElement;
  const system = matchMedia('(prefers-color-scheme: dark)');
  /* A gallery opens a page with ?theme=dark or ?theme=light. That counts as a value the page set. */
  const asked = new URLSearchParams(location.search).get('theme');
  if (!root.hasAttribute('data-theme') && ['light', 'dark'].includes(asked)) root.dataset.theme = asked;
  let pageTheme = root.hasAttribute('data-theme');
  const watch = new MutationObserver(() => { pageTheme = true; watch.disconnect(); });
  if (!pageTheme) watch.observe(root, {attributeFilter: ['data-theme']});
  function applyTheme() {
    if (watch.takeRecords().length) { pageTheme = true; watch.disconnect(); }
    if (pageTheme) return;
    root.dataset.theme = system.matches ? 'dark' : 'light';
    watch.takeRecords();
  }
  system.addEventListener('change', applyTheme);
  const observer = new ResizeObserver(entries => entries.forEach(({target}) => {
    const w = target.clientWidth, h = target.clientHeight;
    const svg = target.querySelector(':scope > .sketch-outline');
    svg.setAttribute('viewBox', `0 0 ${w} ${h}`);
    svg.firstChild.setAttribute('d', `M7 3 Q${w*.18} -.5 ${w*.38} 2.5 T${w*.7} 2 Q${w*.9} .5 ${w-7} 3 Q${w-1} 1 ${w-2} 8 Q${w+1} ${h*.45} ${w-2} ${h-8} Q${w} ${h-2} ${w-8} ${h-2} Q${w*.7} ${h+1} ${w*.5} ${h-2} T7 ${h-2} Q1 ${h-1} 2 ${h-8} Q-1 ${h*.6} 2 9 Q1 2 7 3`);
  }));
  const outlined = '.sketch-frame, .sketch-popover, .sketch-menu, .sketch-dialog, .sketch-toast';
  const outline = frame => {
    if (frame.querySelector(':scope > .sketch-outline')) return;
    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.setAttribute('class', 'sketch-outline');
    svg.setAttribute('aria-hidden', 'true');
    svg.append(document.createElementNS(svg.namespaceURI, 'path'));
    frame.prepend(svg);
    observer.observe(frame);
  };
  /* Line icons, drawn on a 24px grid. <i data-icon="close"></i> becomes the svg. */
  const icons = {
    close: 'M6 6l12 12M18 6L6 18', plus: 'M12 5v14M5 12h14', minus: 'M5 12h14', check: 'M5 12.5l4.5 4.5L19 7',
    'chevron-down': 'M6 9l6 6 6-6', 'chevron-up': 'M6 15l6-6 6 6', 'chevron-left': 'M15 6l-6 6 6 6', 'chevron-right': 'M9 6l6 6-6 6',
    'arrow-left': 'M19 12H5M11 6l-6 6 6 6', 'arrow-right': 'M5 12h14M13 6l6 6-6 6',
    search: 'M10.5 4a6.5 6.5 0 1 0 0 13a6.5 6.5 0 1 0 0-13zM15.5 15.5L20 20', menu: 'M4 7h16M4 12h16M4 17h16',
    more: 'M5 12h1M11.5 12h1M18 12h1', edit: 'M4 20h4L19 9l-4-4L4 16zM13.5 6.5l4 4',
    trash: 'M4 7h16M9 7V4h6v3M6 7l1 13h10l1-13', sliders: 'M4 7h10M18 7h2M16 5v4M4 17h4M12 17h8M10 15v4',
    settings: 'M12 9a3 3 0 1 0 0 6a3 3 0 1 0 0-6zM12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9L7 7M17 17l2.1 2.1M4.9 19.1L7 17M17 7l2.1-2.1',
    comment: 'M4 5h16v11H9l-5 4z', user: 'M12 4a4 4 0 1 0 0 8a4 4 0 1 0 0-8zM4 21c1-4 4-6 8-6s7 2 8 6',
    home: 'M4 11l8-7 8 7M6 9.5V20h12V9.5', bell: 'M6 16v-5a6 6 0 0 1 12 0v5l2 2H4zM10 21h4',
    calendar: 'M4 6h16v14H4zM4 10h16M8 3v4M16 3v4', copy: 'M8 8h12v12H8zM16 8V4H4v12h4',
    link: 'M10 14l4-4M9 7l2-2a4 4 0 0 1 6 6l-2 2M15 17l-2 2a4 4 0 0 1-6-6l2-2',
    upload: 'M12 16V4M7 9l5-5 5 5M4 20h16', download: 'M12 4v12M7 11l5 5 5-5M4 20h16',
    eye: 'M2 12c3-5 6.5-7 10-7s7 2 10 7c-3 5-6.5 7-10 7S5 17 2 12zM12 9a3 3 0 1 0 0 6a3 3 0 1 0 0-6z',
    filter: 'M4 5h16l-6 8v6l-4 2v-8z', external: 'M14 4h6v6M20 4l-9 9M18 14v6H4V6h6',
    info: 'M12 3a9 9 0 1 0 0 18a9 9 0 1 0 0-18zM12 11v6M12 7.5v.5', warning: 'M12 3L2 20h20zM12 10v5M12 17.5v.5',
    image: 'M4 5h16v14H4zM4 16l5-5 4 4 3-3 4 4', send: 'M20 4L4 11l7 2 3 7zM11 13l9-9',
    smile: 'M12 3a9 9 0 1 0 0 18a9 9 0 1 0 0-18zM8 14c1 1.5 2.4 2 4 2s3-.5 4-2M9 9.5v.5M15 9.5v.5', box: 'M4 7.5L12 3l8 4.5v9L12 21l-8-4.5zM4 7.5L12 12l8-4.5M12 12v9',
  };
  const drawIcon = slot => {
    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.setAttribute('class', 'sketch-icon');
    svg.setAttribute('viewBox', '0 0 24 24');
    svg.setAttribute('aria-hidden', 'true');
    const path = document.createElementNS(svg.namespaceURI, 'path');
    path.setAttribute('d', icons[slot.dataset.icon] || icons.image);
    svg.append(path);
    slot.replaceWith(svg);
  };

  /* Popover and menu: a trigger with data-sketch-popover="id" opens the element with that id. */
  let open = null;
  const focusables = root => [...root.querySelectorAll('a[href], button:not(:disabled), input:not(:disabled), select, textarea, [tabindex="0"]')];
  const place = (layer, trigger) => {
    layer.style.maxHeight = `${innerHeight - 16}px`;
    layer.style.overflowY = '';
    if (layer.scrollHeight > layer.clientHeight) layer.style.overflowY = 'auto';
    const t = trigger.getBoundingClientRect(), w = layer.offsetWidth, h = layer.offsetHeight;
    const below = t.bottom + 8, above = t.top - h - 8;
    const top = below + h > innerHeight - 8 && above > 8 ? above : below;
    layer.style.top = `${Math.max(8, Math.min(top, innerHeight - h - 8))}px`;
    const start = t.left + w > innerWidth - 8 ? t.right - w : t.left;
    layer.style.left = `${Math.max(8, Math.min(start, innerWidth - w - 8))}px`;
  };
  const closeLayer = (returnFocus = true) => {
    if (!open) return;
    const {layer, trigger} = open;
    open = null;
    layer.hidden = true;
    trigger.setAttribute('aria-expanded', 'false');
    if (returnFocus) trigger.focus();
  };
  const openLayer = (layer, trigger, moveFocus = true) => {
    closeLayer(false);
    open = {layer, trigger};
    layer.hidden = false;
    trigger.setAttribute('aria-expanded', 'true');
    place(layer, trigger);
    if (moveFocus) focusables(layer)[0]?.focus();
  };
  const menuItems = menu => [...menu.querySelectorAll('.sketch-menu-item:not(:disabled)')];

  /* An open select: sketch.css draws the list where the browser has appearance: base-select.
     Every other browser paints its own list, so a sketch-menu of the options takes its place (#154). */
  const drawnList = !CSS.supports('appearance', 'base-select');
  const ownsList = target => drawnList && target.matches?.('select.sketch-input:not([multiple], :disabled)') && target.size <= 1;
  /* The list takes the field's name: the select's aria-label, or its label's words without the options. */
  const fieldName = select => select.getAttribute('aria-label') || [...select.labels].map(label => {
    const copy = label.cloneNode(true);
    copy.querySelectorAll('select, .sketch-menu').forEach(part => part.remove());
    return copy.textContent.trim();
  }).join(' ');
  let lists = 0;
  const openList = select => {
    if (!select.sketchList) {
      select.sketchList = Object.assign(document.createElement('div'), {className: 'sketch-menu', hidden: true, id: `sketch-list-${++lists}`});
      select.sketchList.setAttribute('role', 'listbox');
      select.setAttribute('aria-controls', select.sketchList.id);
      /* Next to its field, so the list stays in the same dialog and landmark as the select. */
      (select.closest('label') || select).after(select.sketchList);
      outline(select.sketchList);
    }
    const list = select.sketchList;
    list.setAttribute('aria-label', fieldName(select));
    list.querySelectorAll(':scope > :is(.sketch-menu-item, .sketch-menu-group)').forEach(item => item.remove());
    /* A hidden option stays out, and :disabled also covers an option in a disabled optgroup.
       An optgroup becomes a group with its label as a heading. */
    let group = null;
    [...select.options].forEach((option, index) => {
      if (option.hidden) return;
      const optgroup = option.parentElement.closest('optgroup');
      if (optgroup && optgroup !== group?.sketchGroup) {
        group = Object.assign(document.createElement('div'), {className: 'sketch-menu-group', sketchGroup: optgroup});
        group.setAttribute('role', 'group');
        group.setAttribute('aria-label', optgroup.label);
        if (optgroup.disabled) group.setAttribute('aria-disabled', 'true');
        const label = Object.assign(document.createElement('div'), {className: 'sketch-menu-group-label', textContent: optgroup.label});
        label.setAttribute('aria-hidden', 'true');
        group.append(label);
        list.append(group);
      } else if (!optgroup) group = null;
      const item = Object.assign(document.createElement('button'), {type: 'button', className: 'sketch-menu-item', textContent: option.text, disabled: option.matches(':disabled')});
      item.setAttribute('role', 'option');
      item.setAttribute('aria-selected', String(option.selected));
      item.sketchIndex = index;
      (group || list).append(item);
    });
    list.style.minWidth = `${select.offsetWidth}px`;
    openLayer(list, select, false);
    (list.querySelector('[aria-selected="true"]:not(:disabled)') || menuItems(list)[0])?.focus();
  };
  const chooseOption = (select, item) => {
    if (select.selectedIndex === item.sketchIndex) return;
    select.selectedIndex = item.sketchIndex;
    select.dispatchEvent(new Event('input', {bubbles: true}));
    select.dispatchEvent(new Event('change', {bubbles: true}));
  };

  /* A native dialog: data-sketch-open="id" shows it, data-sketch-close closes the nearest one. */
  const showDialog = (dialog, opener) => {
    if (dialog.open) return;
    /* Focus goes back to something that stays visible: the trigger of a menu that held the opener. */
    opener = opener || page.querySelector(`[data-sketch-open="${dialog.id}"]`);
    dialog.sketchOpener = open?.layer.contains(opener) ? open.trigger : opener;
    dialog.showModal();
  };

  /* One toast at a time, announced politely, gone after four seconds. */
  let toastTimer, toastOpener;
  const hideToast = () => {
    const toast = page.querySelector(':scope > .sketch-toast:not([hidden])');
    if (!toast) return false;
    toast.hidden = true;
    clearTimeout(toastTimer);
    toastOpener?.focus();
    return true;
  };
  window.sketchToast = (text, opener) => {
    toastOpener = opener;
    let toast = page.querySelector(':scope > .sketch-toast');
    if (!toast) {
      toast = Object.assign(document.createElement('div'), {className: 'sketch-toast', hidden: true});
      toast.setAttribute('role', 'status');
      toast.append(document.createElement('span'));
      page.append(toast);
      outline(toast);
    }
    toast.lastChild.textContent = text;
    toast.hidden = false;
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => { toast.hidden = true; }, 4000);
  };

  const selectTab = (tab, moveFocus) => {
    tab.closest('[role="tablist"]').querySelectorAll('[role="tab"]').forEach(other => {
      const chosen = other === tab;
      other.setAttribute('aria-selected', String(chosen));
      other.tabIndex = chosen ? 0 : -1;
      const panel = document.getElementById(other.getAttribute('aria-controls'));
      if (panel) panel.hidden = !chosen;
    });
    if (moveFocus) tab.focus();
  };

  page.addEventListener('click', event => {
    const target = event.target;
    /* A menu button opens or closes the .sketch-collapse right after it. */
    const menu = target.closest('.sketch-menu-button');
    if (menu) menu.setAttribute('aria-expanded', String(menu.getAttribute('aria-expanded') !== 'true'));
    const layerTrigger = open?.layer.contains(target) ? open.trigger : null;
    const popoverTrigger = target.closest('[data-sketch-popover]');
    if (popoverTrigger) {
      const layer = document.getElementById(popoverTrigger.dataset.sketchPopover);
      if (open?.layer === layer) closeLayer(); else openLayer(layer, popoverTrigger);
      return;
    }
    const opener = target.closest('[data-sketch-open]');
    if (opener) showDialog(document.getElementById(opener.dataset.sketchOpen), opener);
    if (target.closest('[data-sketch-close]')) {
      const dialog = target.closest('dialog');
      if (dialog) dialog.close(); else closeLayer();
    }
    if (target.matches('dialog.sketch-dialog')) {
      const r = target.getBoundingClientRect();
      if (event.clientX < r.left || event.clientX > r.right || event.clientY < r.top || event.clientY > r.bottom) target.close();
    }
    const option = open && target.closest('[role="option"].sketch-menu-item');
    if (option) chooseOption(open.trigger, option);
    if (open && target.closest('.sketch-menu-item')) closeLayer();
    const chip = target.closest('.sketch-chip[aria-pressed]');
    if (chip) chip.setAttribute('aria-pressed', String(chip.getAttribute('aria-pressed') !== 'true'));
    const tab = target.closest('.sketch-tabs [role="tab"]');
    if (tab) selectTab(tab, false);
    const toast = target.closest('[data-sketch-toast]');
    if (toast) sketchToast(toast.dataset.sketchToast, layerTrigger || toast);
  });
  page.addEventListener('pointerdown', event => {
    if (open && !open.layer.contains(event.target) && !open.trigger.contains(event.target)) closeLayer(false);
  });
  page.addEventListener('mousedown', event => {
    if (!ownsList(event.target)) return;
    event.preventDefault();
    event.target.focus();
    if (open?.trigger === event.target) closeLayer(); else openList(event.target);
  });
  page.addEventListener('keydown', event => {
    if (event.key === 'Escape' && open) { event.preventDefault(); closeLayer(); return; }
    if (event.key === 'Escape' && !event.target.closest('dialog') && hideToast()) { event.preventDefault(); return; }
    if (ownsList(event.target) && [' ', 'Enter', 'ArrowDown', 'ArrowUp'].includes(event.key)) { event.preventDefault(); openList(event.target); return; }
    const menu = event.target.closest('.sketch-menu');
    if (menu && ['ArrowDown', 'ArrowUp', 'Home', 'End'].includes(event.key)) {
      const items = menuItems(menu), at = items.indexOf(event.target);
      const next = {ArrowDown: at + 1, ArrowUp: at - 1, Home: 0, End: items.length - 1}[event.key];
      items[(next + items.length) % items.length]?.focus();
      event.preventDefault();
    }
    const tab = event.target.closest('.sketch-tabs [role="tab"]');
    if (tab && ['ArrowRight', 'ArrowLeft', 'Home', 'End'].includes(event.key)) {
      const tabs = [...tab.parentElement.querySelectorAll('[role="tab"]')], at = tabs.indexOf(tab);
      const next = {ArrowRight: at + 1, ArrowLeft: at - 1, Home: 0, End: tabs.length - 1}[event.key];
      selectTab(tabs[(next + tabs.length) % tabs.length], true);
      event.preventDefault();
    }
  });
  addEventListener('resize', () => open && place(open.layer, open.trigger));

  /* States: each [data-state="id"] is one screen. The address #id shows it; no address shows the
     first. An overlay marked data-open inside a state opens with it, so a review can link to it. */
  const showState = () => {
    const states = [...page.querySelectorAll('[data-state]')];
    if (!states.length) return;
    const current = states.find(state => state.dataset.state === location.hash.slice(1)) || states[0];
    closeLayer(false);
    page.querySelectorAll('dialog[open]').forEach(dialog => dialog.close());
    states.forEach(state => { state.hidden = state !== current; });
    current.querySelectorAll('[data-open]').forEach(layer => {
      if (layer.matches('dialog')) { showDialog(layer, null); return; }
      const trigger = page.querySelector(`[data-sketch-popover="${layer.id}"]`);
      if (trigger) openLayer(layer, trigger, false);
    });
  };
  addEventListener('hashchange', showState);

  window.initSketch = () => {
    page.querySelectorAll('i[data-icon]').forEach(drawIcon);
    page.querySelectorAll(outlined).forEach(outline);
    page.querySelectorAll('.sketch-popover, .sketch-menu').forEach(layer => {
      if (!layer.matches('dialog')) layer.hidden = !open || open.layer !== layer;
      if (!layer.sketchReady) {
        layer.sketchReady = true;
        /* A layer taller than the screen scrolls, and its outline stays on the visible box. */
        layer.addEventListener('scroll', () => {
          const svg = layer.querySelector(':scope > .sketch-outline');
          if (svg) svg.style.transform = `translateY(${layer.scrollTop}px)`;
        });
      }
      if (layer.matches('.sketch-menu:not([role="listbox"])')) {
        layer.setAttribute('role', 'menu');
        layer.querySelectorAll('.sketch-menu-item').forEach(item => item.setAttribute('role', 'menuitem'));
      }
    });
    page.querySelectorAll('[data-sketch-popover]').forEach(trigger => {
      trigger.setAttribute('aria-controls', trigger.dataset.sketchPopover);
      trigger.setAttribute('aria-haspopup', document.getElementById(trigger.dataset.sketchPopover)?.matches('.sketch-menu') ? 'menu' : 'dialog');
      if (!trigger.hasAttribute('aria-expanded')) trigger.setAttribute('aria-expanded', 'false');
    });
    page.querySelectorAll('dialog.sketch-dialog').forEach(dialog => {
      if (dialog.sketchReady) return;
      dialog.sketchReady = true;
      dialog.addEventListener('close', () => dialog.sketchOpener?.focus());
    });
    page.querySelectorAll('.sketch-tabs').forEach(list => {
      list.setAttribute('role', 'tablist');
      const tabs = [...list.querySelectorAll('[role="tab"]')];
      const chosen = tabs.find(tab => tab.getAttribute('aria-selected') === 'true') || tabs[0];
      if (chosen) selectTab(chosen, false);
    });
    applyTheme();
    showState();
  };
  window.initSketch();
})();
