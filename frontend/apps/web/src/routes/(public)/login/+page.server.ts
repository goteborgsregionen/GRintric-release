import { env } from "$env/dynamic/private";
import { loginUser } from "$lib/features/auth/auth.server";
import { getMobilityguardLink } from "$lib/features/auth/oidc.server";
import { redirect, fail, type Actions } from "@sveltejs/kit";

export const actions: Actions = {
  login: async (event) => {
    console.log("Login action in +page.server.ts triggered!"); // Add this line
    const { cookies, request } = event;

    const data = await request.formData();
    const username = data.get("email")?.toString() ?? null;
    const password = data.get("password")?.toString() ?? null;
    // Access 'next' from event.url.searchParams instead of $page
    const next = event.url.searchParams.get("next") ?? null;

    if (username && password) {
      const success = await loginUser(event, username, password);

      if (success) {
        if (next) {
          throw redirect(303, `/${next.slice(1)}`);
        }
        throw redirect(303, "/spaces/personal");
      }
    }

    return fail(400, { failed: true });
  }
};

/* 
    Copyright (c) 2024 Sundsvalls Kommun

    Licensed under the MIT License.
*/
export const load = async (event) => {
  // If user is logged in already: forward to base url, as login doesn't make sense
  if (event.locals.user.isLoggedIn) {
    redirect(302, "/");
  }

  let mobilityguardLink = undefined;
  if (env.MOBILITY_GUARD_AUTH) {
    mobilityguardLink = await getMobilityguardLink(event.url.origin, event.cookies);
  }

  return {
    mobilityguardLink
  };
};
