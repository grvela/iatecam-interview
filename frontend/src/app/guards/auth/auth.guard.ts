import { CanActivateFn } from '@angular/router';

import { AuthService } from 'src/app/services/auth/auth.service';

export const authGuard: CanActivateFn = (route, state) => {
  const authService = new AuthService()

  if (authService.isLoggedInUser()) {
    return true;
  } else {
    return false;
  }
};
